import sys
from PySide6.QtWidgets import QApplication
from modules.main import Player

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(app.exec())
