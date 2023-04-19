off_button_style = """
QPushButton:pressed {
    background-color: #ECF0F1;
}
"""

on_button_style = """
QPushButton {
    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));
}
QPushButton:pressed {
    background-color: #ECF0F1;
}
"""

playlist_style = """
QListView {
    background-color: #11041A;
    color: #ECF0F1;
    font-size: 15px;
}

QListView {
    show-decoration-selected: 1;
}

QListView::item:selected:!active {
    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));
}

QListView::item:selected:active {
    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));
}

QListView::item:hover {
    background: #502274;
}

QListView::item {
    height: 30 px;
}
"""
