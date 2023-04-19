from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import (Qt, QRect, QPropertyAnimation, Property,
                            QPoint, QEasingCurve, Signal)


class Toggle(QCheckBox):
    onToggle = Signal(bool)

    def __init__(self, parent=None):
        QCheckBox.__init__(self)

        self.bg_color = "#777"
        self.circle_color = "#585858"
        self.active_color = "#502274"
        animation_curve = QEasingCurve.InOutCubic

        self.setFixedSize(100, 28)
        self.setCursor(Qt.PointingHandCursor)

        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value: int):
        self.animation.stop()
        if value:
            self.onToggle.emit(True)
            self.animation.setEndValue(self.width() - 26)
        else:
            self.onToggle.emit(False)
            self.animation.setEndValue(3)

        self.animation.start()

    def hitButton(self, p: QPoint):
        return self.contentsRect().contains(p)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            p.setBrush(QColor(self.bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(),
                              self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            p.setBrush(QColor(self.active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(),
                              self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self.circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)

        p.end()
