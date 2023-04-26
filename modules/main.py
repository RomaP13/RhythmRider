import os
import time
import random
from math import ceil
from mutagen.mp3 import MP3
from PySide6.QtCore import Qt, QSettings, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from modules.styles import on_button_style, off_button_style
from modules.player import Ui_MainWindow
from modules.thread import PlayerThread
from modules.playlist import PlayList
from modules.toggle import Toggle


class Player(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__(parent=None)
        self.setupUi(self)
        self.setWindowTitle("RhythmRider")
        self.setWindowIcon(QIcon("assets/play.svg"))
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.settings = QSettings("RomaP13", "RhythmRider")
        self.music_list = []
        self.shuffle_music_list = None
        self.thread = PlayerThread("", 0)
        self.current_song = ""
        self.volume_slider_value = 30
        self.root = self.settings.value("root", "")
        self.playlist_toggle = Toggle()
        self.fadeout_toggle = Toggle()
        self.playlist = PlayList()
        if self.root:
            self.load_playlist()

        self.add_widgets()
        self.set_initial_state()
        self.set_signals()
        self.load_last_played_song()
        self.toggle_playlist()

    def clear_thread(self):
        try:
            self.thread.terminate()
        except AttributeError:
            pass
        self.thread = PlayerThread("", 0)

    def play(self, song_name: str):
        self.set_song_name(song_name)
        self.playlist.set_playing(song_name[:-4])
        song_path = os.path.join(self.root, song_name)
        self.playPauseBtn.setIcon(QIcon("assets/pause.svg"))
        self.playPauseBtn.setStyleSheet("QPushButton {padding:3px;}")
        self.start_music(song_path)

    def pause(self):
        self.thread.pause()
        self.thread.mixer.pause()
        self.playPauseBtn.setIcon(QIcon("assets/play.svg"))
        self.playPauseBtn.setStyleSheet("QPushButton {padding-left:4px;}")

    def play_next_song(self):
        if self.shuffleBtn.isChecked():
            if self.shuffle_music_list:
                index = self.shuffle_music_list.index(self.current_song)
                if index + 1 < len(self.shuffle_music_list):
                    self.play(self.shuffle_music_list[index + 1])
                else:
                    self.play(self.shuffle_music_list[0])
        else:
            if self.music_list:
                index = self.music_list.index(self.current_song)
                if index + 1 < len(self.music_list):
                    self.play(self.music_list[index + 1])
                else:
                    self.play(self.music_list[0])

    def play_previous_song(self):
        if self.shuffleBtn.isChecked():
            if self.shuffle_music_list:
                index = self.shuffle_music_list.index(self.current_song)
                self.play(self.shuffle_music_list[index - 1])
        else:
            if self.music_list:
                index = self.music_list.index(self.current_song)
                self.play(self.music_list[index - 1])

    def play_same_song(self):
        self.play(self.current_song)

    def start_music(self, song_path: str):
        self.clear_thread()
        length = self.get_length(song_path)
        self.progressSlider.setRange(0, length)
        self.set_end_time(length)
        if self.fadeout_toggle.isChecked():
            self.thread = PlayerThread(song_path, length,
                                       fadeout_time=self.fadeoutSlider.value())
        else:
            self.thread = PlayerThread(song_path, length)
        self.thread.positionChanged.connect(self.set_progress)
        self.thread.timeChanged.connect(self.set_start_time)
        self.thread.finished.connect(self.music_end_handler)
        self.thread.start()
        self.toggle_button_state(True)

    def music_end_handler(self):
        # If the song was not interrupted
        if self.thread.position == self.thread.length:
            if self.repeatBtn.isChecked():
                self.play_same_song()
            else:
                self.play_next_song()

    def get_length(self, file: str):
        mp3 = MP3(file)
        return int(mp3.info.length)

    def add_widgets(self):
        self.libraryLayout.addWidget(self.playlist)
        self.playlist.hide()
        self.playlistLayout.addWidget(self.playlist_toggle,
                                      Qt.AlignCenter, Qt.AlignCenter)
        self.fadeoutLayout.addWidget(self.fadeout_toggle,
                                     Qt.AlignCenter, Qt.AlignCenter)

    def set_initial_state(self):
        is_repeat = self.settings.value("is_repeat", False, type=bool)
        is_shuffle = self.settings.value("is_shuffle", False, type=bool)
        is_fadeout = self.settings.value("is_fadeout", False, type=bool)
        fadeout_intensity = self.settings.value("fadeout_intensity", 0,
                                                type=int)
        self.repeatBtn.setCheckable(True)
        self.shuffleBtn.setCheckable(True)
        self.volumeBtn.setCheckable(True)
        self.repeatBtn.setChecked(is_repeat)
        self.shuffleBtn.setChecked(is_shuffle)
        self.fadeout_toggle.setChecked(is_fadeout)
        self.fadeoutSlider.setValue(fadeout_intensity)
        self.playlist_toggle.setChecked(True if self.root else False)
        self.on_repeat()
        self.on_shuffle()

    def set_signals(self):
        self.playlist.textClick.connect(self.play)
        self.volumeBtn.clicked.connect(self.toggle_sound)
        self.previousBtn.clicked.connect(self.play_previous_song)
        self.playPauseBtn.clicked.connect(self.toggle_pause)
        self.nextBtn.clicked.connect(self.play_next_song)
        self.repeatBtn.clicked.connect(self.on_repeat)
        self.shuffleBtn.clicked.connect(self.on_shuffle)
        self.playlistDirectoryBtn.clicked.connect(self.open_directory)
        self.volumeSlider.valueChanged.connect(self.set_volume)
        self.progressSlider.sliderPressed.connect(self.on_slider_pressed)
        self.progressSlider.sliderReleased.connect(self.on_slider_released)
        self.fadeoutSlider.valueChanged.connect(self.set_fadeout_slider_value)
        self.fadeout_toggle.onToggle.connect(self.on_toggle)
        self.githubBtn.clicked.connect(lambda: self.open_url(
            "https://github.com/RomaP13/RhythmRider"))
        self.pyside6Btn.clicked.connect(self.aboutQt)
        self.pygameBtn.clicked.connect(lambda: self.open_url(
            "https://www.pygame.org/"))
        self.mutagenBtn.clicked.connect(lambda: self.open_url(
            "https://mutagen.readthedocs.io/en/latest/"))

    def set_fadeout_slider_value(self, value: int):
        self.fadeoutLabel.setText(f"{value} sec")

    def set_song_name(self, song_name: str):
        self.songNameLabel.setText(song_name[:-4])
        self.current_song = song_name

    def set_end_time(self, length: int):
        minutes, seconds = divmod(length, 60)
        if int(seconds) < 10:
            new_time = f"{int(minutes)}:0{int(seconds)}"
        else:
            new_time = f"{int(minutes)}:{int(seconds)}"
        self.endTimeLabel.setText(new_time)

    def set_start_time(self, duration: int):
        new_time = time.strftime("%M:%S", time.gmtime(duration))
        new_time = new_time[1:] if new_time.startswith("0") else new_time
        self.startTimeLabel.setText(new_time)

    def set_volume(self, value: int):
        if value:
            self.volumeBtn.setIcon(QIcon("assets/volumeOn.svg"))
            self.volumeBtn.setStyleSheet(off_button_style)
        else:
            self.volumeBtn.setIcon(QIcon("assets/volumeOff.svg"))
            self.volumeBtn.setStyleSheet(on_button_style)
        self.thread.mixer.set_volume(value / 100)
        self.volumeLabel.setText(str(value) + "%")

    def set_progress(self, pos: int):
        self.progressSlider.setValue(pos)

    def toggle_pause(self):
        if self.thread.mixer.get_busy():
            self.thread.pause()
            self.thread.mixer.pause()
            self.playPauseBtn.setIcon(QIcon("assets/play.svg"))
            self.playPauseBtn.setStyleSheet("QPushButton {padding-left:4px;}")
        else:
            self.thread.resume()
            self.thread.mixer.unpause()
            self.playPauseBtn.setStyleSheet("QPushButton {padding:3px;}")
            self.playPauseBtn.setIcon(QIcon("assets/pause.svg"))

    def toggle_sound(self):
        if self.thread.mixer.get_volume() > 0:
            self.volumeBtn.setIcon(QIcon("assets/volumeOff.svg"))
            self.volumeBtn.setStyleSheet(on_button_style)
            self.volume_slider_value = self.thread.mixer.get_volume()
            self.thread.mixer.set_volume(0)
            self.volumeSlider.setValue(0)
        else:
            self.volumeBtn.setIcon(QIcon("assets/volumeOn.svg"))
            self.volumeBtn.setStyleSheet(off_button_style)
            self.thread.mixer.set_volume(self.volume_slider_value)
            self.volumeSlider.setValue(ceil(self.volume_slider_value * 100))

    def toggle_button_state(self, is_running: bool):
        if is_running:
            self.volumeBtn.setEnabled(True)
            self.previousBtn.setEnabled(True)
            self.playPauseBtn.setEnabled(True)
            self.nextBtn.setEnabled(True)
            self.progressSlider.setEnabled(True)
            self.volumeSlider.setEnabled(True)
        else:
            self.volumeBtn.setEnabled(False)
            self.previousBtn.setEnabled(False)
            self.playPauseBtn.setEnabled(False)
            self.nextBtn.setEnabled(False)
            self.progressSlider.setEnabled(False)
            self.volumeSlider.setEnabled(False)

        if self.fadeout_toggle.isChecked():
            self.fadeoutSlider.setEnabled(True)
        else:
            self.fadeoutSlider.setEnabled(False)

    def toggle_playlist(self):
        if self.music_list:
            self.label.hide()
            self.playlist.show()
        else:
            self.playlist.hide()
            self.label.show()

    def on_slider_pressed(self):
        if self.thread.isRunning():
            self.thread.pause()

    def on_slider_released(self):
        if self.thread.isRunning():
            position = self.progressSlider.value()
            self.thread.play_song(position)
            self.thread.position = position
            self.thread.resume()

    def on_repeat(self):
        if self.repeatBtn.isChecked():
            self.repeatBtn.setStyleSheet(on_button_style)
        else:
            self.repeatBtn.setStyleSheet(off_button_style)

    def on_shuffle(self):
        if self.shuffleBtn.isChecked():
            self.shuffleBtn.setStyleSheet(on_button_style)
            self.shuffle_music_list = self.music_list.copy()
            random.shuffle(self.shuffle_music_list)
        else:
            self.shuffleBtn.setStyleSheet(off_button_style)

    def on_toggle(self, is_toggle: bool):
        if is_toggle:
            self.fadeoutSlider.setEnabled(True)
        else:
            self.fadeoutSlider.setEnabled(False)

    def open_directory(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.Directory)
        dir.setNameFilter("Music .mp3 (*.mp3)")
        if dir.exec():
            self.root = str(dir.directoryUrl())[26:-2]
            self.load_playlist()
            self.toggle_playlist()
        dir.close()

    def load_last_played_song(self):
        volume = self.settings.value("volume", 30, type=int)
        song_path = self.settings.value("song", "")
        position = self.settings.value("position", 0, type=int)
        if song_path and self.root:
            self.play(os.path.basename(song_path))
            self.progressSlider.setValue(position)
            self.set_start_time(position)
            self.thread.set_position(position)
            self.thread.start()
            self.toggle_button_state(True)
            self.pause()
        else:
            self.thread = PlayerThread("", 0)
            self.toggle_button_state(False)
        self.volumeSlider.setValue(volume)
        self.set_volume(volume)

    def load_playlist(self):
        if self.music_list:
            self.playlist.clear_files()
            self.music_list.clear()

        for file in os.listdir(self.root):
            if file.endswith(".mp3"):
                song_path = os.path.join(self.root, file)
                if os.path.isfile(song_path):
                    self.music_list.append(file)
        self.playlist.add_files(self.music_list)

    def load_settings(self):
        self.settings.clear()
        self.settings.setValue("volume", self.volumeSlider.value())
        if self.playlist_toggle.isChecked():
            self.settings.setValue("song", self.thread.path_song)
            self.settings.setValue("position", self.thread.position)
            self.settings.setValue("is_repeat", self.repeatBtn.isChecked())
            self.settings.setValue("is_shuffle", self.shuffleBtn.isChecked())
            self.settings.setValue("root", self.root)
        if self.fadeout_toggle.isChecked():
            self.settings.setValue("is_fadeout", True)
            self.settings.setValue("fadeout_intensity",
                                   self.fadeoutSlider.value())

    def aboutQt(self, event):
        QMessageBox.aboutQt(self, title="About Qt")

    def open_url(self, url: str):
        QDesktopServices.openUrl(QUrl(url))

    def closeEvent(self, event):
        result = QMessageBox.question(
            self,
            "Confirmation of window closing",
            "Do you really want to close the window? The playback of the track will end.")
        if result == QMessageBox.StandardButton.Yes:
            event.accept()
            self.load_settings()
            self.thread.terminate()
            QMainWindow.closeEvent(self, event)
        else:
            event.ignore()
