import pygame
from PySide6.QtCore import QThread, Signal

pygame.init()
pygame.mixer.init()


class PlayerThread(QThread):
    positionChanged = Signal(int)
    timeChanged = Signal(int)

    def __init__(self, path_song: str, length: int, fadeout_time=0):
        super(PlayerThread, self).__init__(parent=None)
        self.path_song = path_song
        self.length = length
        self.fadeout_time = fadeout_time
        self.paused = False
        self.isPlaying = True
        self.position = 0
        self.mixer = pygame.mixer.music

    def run(self):
        self.mixer.load(self.path_song)
        while self.paused:
            pygame.time.Clock().tick(1)
        self.mixer.play(start=self.position)
        while self.isPlaying:
            if not self.paused:
                self.timeChanged.emit(self.position)
                self.positionChanged.emit(self.position)
                if self.position >= self.length:
                    break
                if self.length - self.position == self.fadeout_time:
                    self.mixer.fadeout(self.fadeout_time * 1000)
                self.position += 1
            pygame.time.Clock().tick(1)
        self.mixer.unload()

    def pause(self):
        self.mixer.pause()
        self.paused = True

    def resume(self):
        self.mixer.unpause()
        self.paused = False

    def play_song(self, pos: int):
        self.mixer.play(start=pos)
        self.position = pos

    def set_position(self, pos: int):
        self.position = pos
