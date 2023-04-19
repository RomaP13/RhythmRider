from PySide6.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.btn = QPushButton("Replace")
        self.btn.setCheckable(True)
        self.label = QLabel("TEST")
        self.playlist = QListView()

        self.box1 = QVBoxLayout()
        self.box1.addWidget(self.btn)

        self.box2 = QVBoxLayout()
        self.box2.addWidget(self.label)
        self.box2.addWidget(self.playlist)
        self.playlist.hide()

        self.box3 = QHBoxLayout()
        self.box3.addLayout(self.box1)
        self.box3.addLayout(self.box2)

        self.btn.clicked.connect(self.change)

        self.setLayout(self.box3)

    def change(self):
        if self.btn.isChecked():
            self.label.hide()
            self.playlist.show()
        else:
            self.playlist.hide()
            self.label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
