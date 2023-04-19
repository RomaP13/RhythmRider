import os
from PySide6.QtCore import Signal, QAbstractListModel, Qt, QModelIndex
from PySide6.QtWidgets import QListView
from modules.styles import playlist_style


class PlayModel(QAbstractListModel):
    def __init__(self, songs=None):
        super(PlayModel, self).__init__(parent=None)
        self.songs = songs or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.songs[index.row()]
            return text

    def rowCount(self, index=QModelIndex()):
        return len(self.songs)


class PlayList(QListView):
    textClick = Signal(str)

    def __init__(self):
        super(PlayList, self).__init__(parent=None)
        self.setVisible(True)
        self.setStyleSheet(playlist_style)
        self.model = PlayModel()
        self.setModel(self.model)
        self.clicked.connect(self.callback)

    def callback(self, song):
        self.textClick.emit(song.data() + ".mp3")
        self.model.layoutChanged.emit()

    def add_files(self, files: list):
        for file in files:
            if file.endswith(".mp3"):
                self.model.songs.append(os.path.basename(file)[:-4])
                self.model.layoutChanged.emit()

    def clear_files(self):
        self.model.songs.clear()
        self.model.layoutChanged.emit()

    # This function displays which song is currently playing in the playlist
    def set_playing(self, current_song: str):
        for i in range(self.model.rowCount()):
            index = self.model.index(i)
            if index.data() == current_song:
                self.setCurrentIndex(self.model.index(i))
                break
