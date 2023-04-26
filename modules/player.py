# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 500)
        MainWindow.setMinimumSize(QSize(550, 500))
        MainWindow.setMaximumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(550, 500))
        self.centralwidget.setMaximumSize(QSize(550, 500))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 550, 500))
        self.tabWidget.setMinimumSize(QSize(550, 500))
        self.tabWidget.setMaximumSize(QSize(550, 500))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 43px solid #200e2d;\n"
"    border-radius: 0px;\n"
"    position: absolute;\n"
"    top: -43px;\n"
"    background: rgba( 0, 0, 0, 100% );\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 2px solid #251101;\n"
"    border-radius: 6px;\n"
"    background-color: #3b3561;\n"
"    padding: 4px;\n"
"    color: #ECF0F1;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 6px; \n"
"}")
        self.tabWidget.setIconSize(QSize(25, 25))
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.homeTab.setMinimumSize(QSize(550, 500))
        self.homeTab.setMaximumSize(QSize(550, 500))
        self.homeTab.setStyleSheet(u"border: none;\n"
"")
        self.libraryWidget = QWidget(self.homeTab)
        self.libraryWidget.setObjectName(u"libraryWidget")
        self.libraryWidget.setGeometry(QRect(0, 0, 550, 350))
        self.libraryWidget.setStyleSheet(u"#libraryWidget {\n"
"border: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    width: 10px;\n"
"    border: none;\n"
"    background-color: #11041A;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));\n"
"    border-radius: 0px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-page {\n"
"    background-color: #11041A;\n"
"}\n"
"\n"
"QScrollBar::sub-page {\n"
"    background-color: #11041A;\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: #11041A;\n"
"    color: #ECF0F1;\n"
"    font-size: 20px;\n"
"}")
        self.scrollArea = QScrollArea(self.libraryWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, -1, 550, 351))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 550, 351))
        self.horizontalLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 0, 552, 352))
        self.libraryLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.libraryLayout.setSpacing(0)
        self.libraryLayout.setObjectName(u"libraryLayout")
        self.libraryLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(550, 350))
        self.label.setMaximumSize(QSize(550, 400))
        self.label.setStyleSheet(u"")
        self.label.setWordWrap(True)

        self.libraryLayout.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.playerActionsFrame = QFrame(self.homeTab)
        self.playerActionsFrame.setObjectName(u"playerActionsFrame")
        self.playerActionsFrame.setGeometry(QRect(0, 360, 551, 111))
        self.playerActionsFrame.setStyleSheet(u"#playerActionsFrame {\n"
"    background: #200e2d;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ECF0F1;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: #212121;\n"
"	border-radius: 15px;\n"
"    color: #555555;\n"
"    text-align: centre;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ECF0F1;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    border-radius: 5px;\n"
"    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgb(148, 0, 211), stop:1 rgb(172, 64, 159));\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                     stop: 0 #ddd, stop: 1 #888);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    backgr"
                        "ound-color: #888;\n"
"    border: 1px solid #555;\n"
"    width: 16px;\n"
"    margin-top: -4px;\n"
"    margin-bottom: -4px;\n"
"    border-radius: 8px;\n"
"}")
        self.playerActionsFrame.setFrameShape(QFrame.StyledPanel)
        self.playerActionsFrame.setFrameShadow(QFrame.Raised)
        self.progressWidget = QWidget(self.playerActionsFrame)
        self.progressWidget.setObjectName(u"progressWidget")
        self.progressWidget.setGeometry(QRect(-1, -11, 550, 51))
        self.horizontalLayoutWidget_2 = QWidget(self.progressWidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 20, 551, 31))
        self.progressLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.progressLayout.setSpacing(7)
        self.progressLayout.setObjectName(u"progressLayout")
        self.progressLayout.setContentsMargins(3, 0, 1, 0)
        self.startTimeLabel = QLabel(self.horizontalLayoutWidget_2)
        self.startTimeLabel.setObjectName(u"startTimeLabel")
        self.startTimeLabel.setMaximumSize(QSize(30, 30))

        self.progressLayout.addWidget(self.startTimeLabel)

        self.progressSlider = QSlider(self.horizontalLayoutWidget_2)
        self.progressSlider.setObjectName(u"progressSlider")
        self.progressSlider.setMouseTracking(False)
        self.progressSlider.setTabletTracking(False)
        self.progressSlider.setAcceptDrops(False)
        self.progressSlider.setAutoFillBackground(False)
        self.progressSlider.setStyleSheet(u"")
        self.progressSlider.setMaximum(100)
        self.progressSlider.setTracking(True)
        self.progressSlider.setOrientation(Qt.Horizontal)

        self.progressLayout.addWidget(self.progressSlider)

        self.endTimeLabel = QLabel(self.horizontalLayoutWidget_2)
        self.endTimeLabel.setObjectName(u"endTimeLabel")
        self.endTimeLabel.setMaximumSize(QSize(30, 30))

        self.progressLayout.addWidget(self.endTimeLabel)

        self.actionsWidget = QWidget(self.playerActionsFrame)
        self.actionsWidget.setObjectName(u"actionsWidget")
        self.actionsWidget.setGeometry(QRect(0, 39, 550, 91))
        self.actionsWidget.setMaximumSize(QSize(550, 100))
        self.actionsWidget.setStyleSheet(u"#mainActionsWidget, #secondaryActionsWidget, #volumeWidget {\n"
"    border: 5px solid #251101;\n"
"    border-radius: 25px;\n"
"    background: #502274;\n"
"}")
        self.mainActionsWidget = QWidget(self.actionsWidget)
        self.mainActionsWidget.setObjectName(u"mainActionsWidget")
        self.mainActionsWidget.setGeometry(QRect(205, -2, 140, 50))
        self.mainActionsWidget.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.mainActionsWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 141, 51))
        self.mainActionsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.mainActionsLayout.setSpacing(0)
        self.mainActionsLayout.setObjectName(u"mainActionsLayout")
        self.mainActionsLayout.setContentsMargins(0, 0, 0, 0)
        self.previousBtn = QPushButton(self.horizontalLayoutWidget)
        self.previousBtn.setObjectName(u"previousBtn")
        self.previousBtn.setMaximumSize(QSize(30, 30))
        self.previousBtn.setStyleSheet(u"padding-right: 3px\n"
"")
        icon = QIcon()
        icon.addFile(u"assets/previous.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previousBtn.setIcon(icon)
        self.previousBtn.setIconSize(QSize(20, 20))

        self.mainActionsLayout.addWidget(self.previousBtn)

        self.playPauseBtn = QPushButton(self.horizontalLayoutWidget)
        self.playPauseBtn.setObjectName(u"playPauseBtn")
        self.playPauseBtn.setMinimumSize(QSize(0, 0))
        self.playPauseBtn.setMaximumSize(QSize(30, 30))
        self.playPauseBtn.setToolTipDuration(-1)
#if QT_CONFIG(statustip)
        self.playPauseBtn.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.playPauseBtn.setStyleSheet(u"padding-left: 4px\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"assets/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playPauseBtn.setIcon(icon1)
        self.playPauseBtn.setIconSize(QSize(20, 20))

        self.mainActionsLayout.addWidget(self.playPauseBtn)

        self.nextBtn = QPushButton(self.horizontalLayoutWidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMaximumSize(QSize(30, 30))
        self.nextBtn.setStyleSheet(u"padding-left: 3px\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"assets/next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon2)
        self.nextBtn.setIconSize(QSize(20, 20))

        self.mainActionsLayout.addWidget(self.nextBtn)

        self.volumeWidget = QWidget(self.actionsWidget)
        self.volumeWidget.setObjectName(u"volumeWidget")
        self.volumeWidget.setGeometry(QRect(0, -2, 180, 50))
        self.horizontalLayoutWidget_3 = QWidget(self.volumeWidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 0, 121, 51))
        self.volumeLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.volumeLayout.setSpacing(2)
        self.volumeLayout.setObjectName(u"volumeLayout")
        self.volumeLayout.setContentsMargins(0, 0, 0, 0)
        self.volumeBtn = QPushButton(self.horizontalLayoutWidget_3)
        self.volumeBtn.setObjectName(u"volumeBtn")
        self.volumeBtn.setMinimumSize(QSize(30, 30))
        self.volumeBtn.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"assets/volumeOn.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.volumeBtn.setIcon(icon3)
        self.volumeBtn.setIconSize(QSize(20, 20))

        self.volumeLayout.addWidget(self.volumeBtn)

        self.volumeSlider = QSlider(self.horizontalLayoutWidget_3)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.volumeLayout.addWidget(self.volumeSlider)

        self.volumeLabel = QLabel(self.volumeWidget)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setGeometry(QRect(133, 10, 40, 30))
        self.volumeLabel.setMaximumSize(QSize(40, 30))
        self.volumeLabel.setStyleSheet(u"")
        self.secondaryActionsWidget = QWidget(self.actionsWidget)
        self.secondaryActionsWidget.setObjectName(u"secondaryActionsWidget")
        self.secondaryActionsWidget.setGeometry(QRect(370, -2, 180, 50))
        self.horizontalLayoutWidget_4 = QWidget(self.secondaryActionsWidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 0, 181, 51))
        self.secondaryActionsLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.secondaryActionsLayout.setSpacing(0)
        self.secondaryActionsLayout.setObjectName(u"secondaryActionsLayout")
        self.secondaryActionsLayout.setContentsMargins(0, 0, 0, 0)
        self.repeatBtn = QPushButton(self.horizontalLayoutWidget_4)
        self.repeatBtn.setObjectName(u"repeatBtn")
        self.repeatBtn.setMaximumSize(QSize(30, 30))
        self.repeatBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"assets/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.repeatBtn.setIcon(icon4)
        self.repeatBtn.setIconSize(QSize(25, 25))
        self.repeatBtn.setCheckable(True)

        self.secondaryActionsLayout.addWidget(self.repeatBtn)

        self.shuffleBtn = QPushButton(self.horizontalLayoutWidget_4)
        self.shuffleBtn.setObjectName(u"shuffleBtn")
        self.shuffleBtn.setMaximumSize(QSize(30, 30))
        self.shuffleBtn.setStyleSheet(u"padding-left: 2px;")
        icon5 = QIcon()
        icon5.addFile(u"assets/shuffle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.shuffleBtn.setIcon(icon5)
        self.shuffleBtn.setIconSize(QSize(24, 24))
        self.shuffleBtn.setCheckable(True)

        self.secondaryActionsLayout.addWidget(self.shuffleBtn)

        self.playlistDirectoryBtn = QPushButton(self.horizontalLayoutWidget_4)
        self.playlistDirectoryBtn.setObjectName(u"playlistDirectoryBtn")
        self.playlistDirectoryBtn.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u"assets/playlist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playlistDirectoryBtn.setIcon(icon6)
        self.playlistDirectoryBtn.setIconSize(QSize(25, 25))

        self.secondaryActionsLayout.addWidget(self.playlistDirectoryBtn)

        self.songNameWidget = QWidget(self.homeTab)
        self.songNameWidget.setObjectName(u"songNameWidget")
        self.songNameWidget.setGeometry(QRect(0, 349, 550, 21))
        self.songNameWidget.setStyleSheet(u"#songNameWidget {\n"
"    border: 2px solid #251101;\n"
"    border-radius: 10px;\n"
"    background: #502274;\n"
"}")
        self.songNameLabel = QLabel(self.songNameWidget)
        self.songNameLabel.setObjectName(u"songNameLabel")
        self.songNameLabel.setGeometry(QRect(0, 0, 551, 20))
        self.songNameLabel.setStyleSheet(u"color: #ECF0F1;\n"
"font-weight: bold;\n"
"")
        self.songNameLabel.setAlignment(Qt.AlignCenter)
        icon7 = QIcon()
        icon7.addFile(u"assets/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.homeTab, icon7, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.mainSettingsWidget = QWidget(self.settingsTab)
        self.mainSettingsWidget.setObjectName(u"mainSettingsWidget")
        self.mainSettingsWidget.setGeometry(QRect(0, 0, 551, 471))
        self.mainSettingsWidget.setStyleSheet(u"#mainSettingsWidget {\n"
"    background-color: #110e1a;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ECF0F1;\n"
"}\n"
"")
        self.mainSettingsFrame = QFrame(self.mainSettingsWidget)
        self.mainSettingsFrame.setObjectName(u"mainSettingsFrame")
        self.mainSettingsFrame.setGeometry(QRect(70, 39, 410, 390))
        self.mainSettingsFrame.setMaximumSize(QSize(800, 800))
        self.mainSettingsFrame.setStyleSheet(u"#mainSettingsFrame {\n"
"    border: 3px solid #6320EE;\n"
"    border-radius: 18px;\n"
"}\n"
"\n"
"#titleFrame_1, #titleFrame_2, #titleFrame_3 {\n"
"    border: 3px solid #251101;\n"
"    border-radius: 15px;\n"
"    background-color: #502274;\n"
"}\n"
"\n"
"#descriptionWidget_1, #descriptionWidget_2, #descriptionWidget_3,\n"
"#checkBoxWidget_1, #checkBoxWidget_2, #sliderWidget{\n"
"    background-color: #3b3561;\n"
"    border-radius: 15px;\n"
"}")
        self.mainSettingsFrame.setFrameShape(QFrame.StyledPanel)
        self.mainSettingsFrame.setFrameShadow(QFrame.Raised)
        self.settingsFrame_1 = QFrame(self.mainSettingsFrame)
        self.settingsFrame_1.setObjectName(u"settingsFrame_1")
        self.settingsFrame_1.setGeometry(QRect(0, 0, 411, 131))
        self.settingsFrame_1.setStyleSheet(u"#settingsFrame_1 {\n"
"    border: 0px solid #6320EE;\n"
"    border-top-left-radius: 18px;\n"
"    border-top-right-radius: 18px;\n"
"}")
        self.settingsFrame_1.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame_1.setFrameShadow(QFrame.Raised)
        self.descriptionWidget_1 = QWidget(self.settingsFrame_1)
        self.descriptionWidget_1.setObjectName(u"descriptionWidget_1")
        self.descriptionWidget_1.setGeometry(QRect(10, 50, 180, 70))
        self.descriptionWidget_1.setMaximumSize(QSize(210, 70))
        self.descriptionLabel_1 = QLabel(self.descriptionWidget_1)
        self.descriptionLabel_1.setObjectName(u"descriptionLabel_1")
        self.descriptionLabel_1.setGeometry(QRect(10, 10, 161, 51))
        self.descriptionLabel_1.setStyleSheet(u"font-size: 12px;\n"
"")
        self.descriptionLabel_1.setWordWrap(True)
        self.titleFrame_1 = QFrame(self.settingsFrame_1)
        self.titleFrame_1.setObjectName(u"titleFrame_1")
        self.titleFrame_1.setGeometry(QRect(9, 10, 390, 31))
        self.titleFrame_1.setFrameShape(QFrame.StyledPanel)
        self.titleFrame_1.setFrameShadow(QFrame.Raised)
        self.titleLabel_1 = QLabel(self.titleFrame_1)
        self.titleLabel_1.setObjectName(u"titleLabel_1")
        self.titleLabel_1.setGeometry(QRect(0, 0, 391, 31))
        self.titleLabel_1.setMaximumSize(QSize(500, 130))
        self.titleLabel_1.setStyleSheet(u"font-size: 16px;\n"
"font-weight:bold;\n"
"\n"
"")
        self.titleLabel_1.setAlignment(Qt.AlignCenter)
        self.titleLabel_1.setWordWrap(True)
        self.checkBoxWidget_1 = QWidget(self.settingsFrame_1)
        self.checkBoxWidget_1.setObjectName(u"checkBoxWidget_1")
        self.checkBoxWidget_1.setGeometry(QRect(219, 50, 180, 70))
        self.horizontalLayoutWidget_6 = QWidget(self.checkBoxWidget_1)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 10, 161, 51))
        self.playlistLayout = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.playlistLayout.setObjectName(u"playlistLayout")
        self.playlistLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsFrame_2 = QFrame(self.mainSettingsFrame)
        self.settingsFrame_2.setObjectName(u"settingsFrame_2")
        self.settingsFrame_2.setGeometry(QRect(-1, 129, 411, 131))
        self.settingsFrame_2.setStyleSheet(u"#settingsFrame_2 {\n"
"border: 2px solid #6320EE;\n"
"}")
        self.settingsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame_2.setFrameShadow(QFrame.Raised)
        self.titleFrame_2 = QFrame(self.settingsFrame_2)
        self.titleFrame_2.setObjectName(u"titleFrame_2")
        self.titleFrame_2.setGeometry(QRect(9, 10, 391, 31))
        self.titleFrame_2.setFrameShape(QFrame.StyledPanel)
        self.titleFrame_2.setFrameShadow(QFrame.Raised)
        self.titleLabel_2 = QLabel(self.titleFrame_2)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.titleLabel_2.setGeometry(QRect(-3, 0, 391, 31))
        self.titleLabel_2.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"")
        self.titleLabel_2.setAlignment(Qt.AlignCenter)
        self.descriptionWidget_2 = QWidget(self.settingsFrame_2)
        self.descriptionWidget_2.setObjectName(u"descriptionWidget_2")
        self.descriptionWidget_2.setGeometry(QRect(10, 50, 180, 70))
        self.descriptionWidget_2.setMaximumSize(QSize(210, 70))
        self.descriptionLabel_2 = QLabel(self.descriptionWidget_2)
        self.descriptionLabel_2.setObjectName(u"descriptionLabel_2")
        self.descriptionLabel_2.setGeometry(QRect(10, 0, 171, 71))
        self.descriptionLabel_2.setMaximumSize(QSize(210, 90))
        self.descriptionLabel_2.setStyleSheet(u"font-size: 12px;\n"
"")
        self.descriptionLabel_2.setWordWrap(True)
        self.checkBoxWidget_2 = QWidget(self.settingsFrame_2)
        self.checkBoxWidget_2.setObjectName(u"checkBoxWidget_2")
        self.checkBoxWidget_2.setGeometry(QRect(220, 50, 180, 70))
        self.horizontalLayoutWidget_7 = QWidget(self.checkBoxWidget_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 10, 161, 51))
        self.fadeoutLayout = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.fadeoutLayout.setObjectName(u"fadeoutLayout")
        self.fadeoutLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsFrame_3 = QFrame(self.mainSettingsFrame)
        self.settingsFrame_3.setObjectName(u"settingsFrame_3")
        self.settingsFrame_3.setGeometry(QRect(-1, 259, 411, 131))
        self.settingsFrame_3.setStyleSheet(u"#settingsFrame_3 {\n"
"    border: 0px solid #6320EE;\n"
"    border-bottom-left-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"}")
        self.settingsFrame_3.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame_3.setFrameShadow(QFrame.Raised)
        self.titleFrame_3 = QFrame(self.settingsFrame_3)
        self.titleFrame_3.setObjectName(u"titleFrame_3")
        self.titleFrame_3.setGeometry(QRect(10, 10, 391, 31))
        self.titleFrame_3.setFrameShape(QFrame.StyledPanel)
        self.titleFrame_3.setFrameShadow(QFrame.Raised)
        self.titleLabel_3 = QLabel(self.titleFrame_3)
        self.titleLabel_3.setObjectName(u"titleLabel_3")
        self.titleLabel_3.setGeometry(QRect(-3, -1, 391, 31))
        self.titleLabel_3.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"")
        self.titleLabel_3.setAlignment(Qt.AlignCenter)
        self.descriptionWidget_3 = QWidget(self.settingsFrame_3)
        self.descriptionWidget_3.setObjectName(u"descriptionWidget_3")
        self.descriptionWidget_3.setGeometry(QRect(10, 50, 180, 70))
        self.descriptionWidget_3.setMaximumSize(QSize(210, 70))
        self.descriptionLabel_3 = QLabel(self.descriptionWidget_3)
        self.descriptionLabel_3.setObjectName(u"descriptionLabel_3")
        self.descriptionLabel_3.setGeometry(QRect(10, -10, 161, 90))
        self.descriptionLabel_3.setMaximumSize(QSize(210, 90))
        self.descriptionLabel_3.setStyleSheet(u"font-size: 12px;\n"
"")
        self.descriptionLabel_3.setWordWrap(True)
        self.sliderWidget = QWidget(self.settingsFrame_3)
        self.sliderWidget.setObjectName(u"sliderWidget")
        self.sliderWidget.setGeometry(QRect(220, 50, 180, 70))
        self.horizontalLayoutWidget_8 = QWidget(self.sliderWidget)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(9, 20, 121, 31))
        self.fadeoutSliderLayout = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.fadeoutSliderLayout.setObjectName(u"fadeoutSliderLayout")
        self.fadeoutSliderLayout.setContentsMargins(0, 0, 0, 0)
        self.fadeoutSlider = QSlider(self.horizontalLayoutWidget_8)
        self.fadeoutSlider.setObjectName(u"fadeoutSlider")
        self.fadeoutSlider.setStyleSheet(u"QSlider::sub-page:horizontal {\n"
"    border-radius: 5px;\n"
"    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgb(148, 0, 211), stop:1 rgb(172, 64, 159));\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                     stop: 0 #ddd, stop: 1 #888);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #888;\n"
"    border: 1px solid #555;\n"
"    width: 16px;\n"
"    margin-top: -4px;\n"
"    margin-bottom: -4px;\n"
"    border-radius: 8px;\n"
"}")
        self.fadeoutSlider.setMinimum(0)
        self.fadeoutSlider.setMaximum(10)
        self.fadeoutSlider.setPageStep(2)
        self.fadeoutSlider.setTracking(True)
        self.fadeoutSlider.setOrientation(Qt.Horizontal)
        self.fadeoutSlider.setInvertedAppearance(False)
        self.fadeoutSlider.setInvertedControls(False)
        self.fadeoutSlider.setTickPosition(QSlider.NoTicks)
        self.fadeoutSlider.setTickInterval(1)

        self.fadeoutSliderLayout.addWidget(self.fadeoutSlider)

        self.fadeoutLabel = QLabel(self.sliderWidget)
        self.fadeoutLabel.setObjectName(u"fadeoutLabel")
        self.fadeoutLabel.setGeometry(QRect(133, 25, 51, 20))
        icon8 = QIcon()
        icon8.addFile(u"assets/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.settingsTab, icon8, "")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.mainAboutWidget = QWidget(self.aboutTab)
        self.mainAboutWidget.setObjectName(u"mainAboutWidget")
        self.mainAboutWidget.setGeometry(QRect(0, 0, 551, 471))
        self.mainAboutWidget.setStyleSheet(u"#mainAboutWidget {\n"
"    background-color: #11041a;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ECF0F1;\n"
"}\n"
"")
        self.mainAboutFrame = QFrame(self.mainAboutWidget)
        self.mainAboutFrame.setObjectName(u"mainAboutFrame")
        self.mainAboutFrame.setGeometry(QRect(70, 39, 410, 390))
        self.mainAboutFrame.setStyleSheet(u"#mainAboutFrame {\n"
"    border: 3px solid #6320EE;\n"
"    border-radius: 18px;\n"
"}\n"
"\n"
"#titleLabel_4, #titleLabel_5 {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#titleFrame_4, #titleFrame_5 {\n"
"    border: 3px solid #251101;\n"
"    border-radius: 15px;\n"
"    background-color: #502274;\n"
"}\n"
"\n"
"#aboutPlayerWidget, #aboutPlayerWidget_2 {\n"
"    background-color: #3b3561;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#pyside6Widget, #pygameWidget, #mutagenWidget {\n"
"    background-color: #3b3561;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#mutagenBtn, #pygameBtn, #pyside6Btn {\n"
"    border-style: none;\n"
"    background-color: transparent;\n"
"    color: #ECF0F1;\n"
"    font-size: 18px;\n"
"}")
        self.mainAboutFrame.setFrameShape(QFrame.StyledPanel)
        self.mainAboutFrame.setFrameShadow(QFrame.Raised)
        self.titleFrame_4 = QFrame(self.mainAboutFrame)
        self.titleFrame_4.setObjectName(u"titleFrame_4")
        self.titleFrame_4.setGeometry(QRect(9, 10, 390, 31))
        self.titleFrame_4.setStyleSheet(u"#titleFrame {\n"
"border: 3px solid #251101;\n"
"border-radius: 15px;\n"
"background-color: #502274;\n"
"}")
        self.titleFrame_4.setFrameShape(QFrame.StyledPanel)
        self.titleFrame_4.setFrameShadow(QFrame.Raised)
        self.titleLabel_4 = QLabel(self.titleFrame_4)
        self.titleLabel_4.setObjectName(u"titleLabel_4")
        self.titleLabel_4.setGeometry(QRect(130, -1, 131, 30))
        self.titleLabel_4.setStyleSheet(u"")
        self.titleLabel_4.setAlignment(Qt.AlignCenter)
        self.aboutPlayerWidget = QWidget(self.mainAboutFrame)
        self.aboutPlayerWidget.setObjectName(u"aboutPlayerWidget")
        self.aboutPlayerWidget.setGeometry(QRect(10, 59, 281, 110))
        self.aboutPlayerWidget.setStyleSheet(u"")
        self.aboutPlayerLabel = QLabel(self.aboutPlayerWidget)
        self.aboutPlayerLabel.setObjectName(u"aboutPlayerLabel")
        self.aboutPlayerLabel.setGeometry(QRect(10, 0, 271, 111))
        self.aboutPlayerLabel.setStyleSheet(u"font-size: 18px;")
        self.aboutPlayerLabel.setWordWrap(True)
        self.titleFrame_5 = QFrame(self.mainAboutFrame)
        self.titleFrame_5.setObjectName(u"titleFrame_5")
        self.titleFrame_5.setGeometry(QRect(10, 190, 390, 30))
        self.titleFrame_5.setStyleSheet(u"")
        self.titleFrame_5.setFrameShape(QFrame.StyledPanel)
        self.titleFrame_5.setFrameShadow(QFrame.Raised)
        self.titleLabel_5 = QLabel(self.titleFrame_5)
        self.titleLabel_5.setObjectName(u"titleLabel_5")
        self.titleLabel_5.setGeometry(QRect(130, -1, 141, 30))
        self.titleLabel_5.setStyleSheet(u"")
        self.titleLabel_5.setAlignment(Qt.AlignCenter)
        self.pyside6Widget = QWidget(self.mainAboutFrame)
        self.pyside6Widget.setObjectName(u"pyside6Widget")
        self.pyside6Widget.setGeometry(QRect(9, 240, 390, 40))
        self.pyside6Widget.setStyleSheet(u"")
        self.pyside6Btn = QPushButton(self.pyside6Widget)
        self.pyside6Btn.setObjectName(u"pyside6Btn")
        self.pyside6Btn.setGeometry(QRect(160, 10, 70, 20))
        self.pyside6Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pyside6Btn.setMouseTracking(True)
        self.pyside6Btn.setStyleSheet(u"")
        self.pygameWidget = QWidget(self.mainAboutFrame)
        self.pygameWidget.setObjectName(u"pygameWidget")
        self.pygameWidget.setGeometry(QRect(9, 290, 390, 40))
        self.pygameWidget.setStyleSheet(u"")
        self.pygameBtn = QPushButton(self.pygameWidget)
        self.pygameBtn.setObjectName(u"pygameBtn")
        self.pygameBtn.setGeometry(QRect(160, 10, 70, 20))
        self.pygameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pygameBtn.setMouseTracking(True)
        self.pygameBtn.setStyleSheet(u"")
        self.mutagenWidget = QWidget(self.mainAboutFrame)
        self.mutagenWidget.setObjectName(u"mutagenWidget")
        self.mutagenWidget.setGeometry(QRect(9, 340, 390, 40))
        self.mutagenWidget.setStyleSheet(u"")
        self.mutagenBtn = QPushButton(self.mutagenWidget)
        self.mutagenBtn.setObjectName(u"mutagenBtn")
        self.mutagenBtn.setGeometry(QRect(155, 10, 80, 20))
        self.mutagenBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mutagenBtn.setMouseTracking(True)
        self.mutagenBtn.setStyleSheet(u"")
        self.aboutPlayerWidget_2 = QWidget(self.mainAboutFrame)
        self.aboutPlayerWidget_2.setObjectName(u"aboutPlayerWidget_2")
        self.aboutPlayerWidget_2.setGeometry(QRect(315, 80, 70, 70))
        self.aboutPlayerWidget_2.setStyleSheet(u"")
        self.githubBtn = QPushButton(self.aboutPlayerWidget_2)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setGeometry(QRect(15, 15, 40, 40))
        self.githubBtn.setToolTipDuration(-1)
        self.githubBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #212121;\n"
"	border-radius: 10px;\n"
"    color: #555555;\n"
"    text-align: centre;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.457, y1:0.222, x2:1, y2:1, stop:0 rgba(148, 0, 211, 255), stop:1 rgba(172, 64, 159, 1));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ECF0F1;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"assets/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.githubBtn.setIcon(icon9)
        self.githubBtn.setIconSize(QSize(33, 33))
        icon10 = QIcon()
        icon10.addFile(u"assets/about.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.aboutTab, icon10, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Click the playlist button to open your music folder", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
#if QT_CONFIG(tooltip)
        self.previousBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.previousBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.previousBtn.setText("")
#if QT_CONFIG(tooltip)
        self.playPauseBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.playPauseBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.playPauseBtn.setText("")
#if QT_CONFIG(tooltip)
        self.nextBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.nextBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.nextBtn.setText("")
#if QT_CONFIG(tooltip)
        self.volumeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.volumeBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.volumeBtn.setText("")
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"100%", None))
#if QT_CONFIG(whatsthis)
        self.repeatBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.repeatBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.shuffleBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.shuffleBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.playlistDirectoryBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.playlistDirectoryBtn.setText("")
        self.songNameLabel.setText(QCoreApplication.translate("MainWindow", u"The song name will be here", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.descriptionLabel_1.setText(QCoreApplication.translate("MainWindow", u"Enabling this option allows the player to save your playlist when you exit.", None))
        self.titleLabel_1.setText(QCoreApplication.translate("MainWindow", u"Save playlist", None))
        self.titleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Fade out", None))
        self.descriptionLabel_2.setText(QCoreApplication.translate("MainWindow", u"This setting adds a smooth fade out effect when music playback finishes. ", None))
        self.titleLabel_3.setText(QCoreApplication.translate("MainWindow", u"Adjust  fade out", None))
        self.descriptionLabel_3.setText(QCoreApplication.translate("MainWindow", u"Set how long the music fades out when playback finishes. For this setting, you need to enable fade out.", None))
        self.fadeoutLabel.setText(QCoreApplication.translate("MainWindow", u"0 sec", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.titleLabel_4.setText(QCoreApplication.translate("MainWindow", u"RhythmRider", None))
        self.aboutPlayerLabel.setText(QCoreApplication.translate("MainWindow", u"The convenient and easy-to-use music player for listening to your favorite songs and artists.", None))
        self.titleLabel_5.setText(QCoreApplication.translate("MainWindow", u"Used libraries", None))
#if QT_CONFIG(tooltip)
        self.pyside6Btn.setToolTip(QCoreApplication.translate("MainWindow", u"About Qt", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pyside6Btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pyside6Btn.setText(QCoreApplication.translate("MainWindow", u"PySide6", None))
#if QT_CONFIG(tooltip)
        self.pygameBtn.setToolTip(QCoreApplication.translate("MainWindow", u"https://www.pygame.org/", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pygameBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pygameBtn.setText(QCoreApplication.translate("MainWindow", u"pygame", None))
#if QT_CONFIG(tooltip)
        self.mutagenBtn.setToolTip(QCoreApplication.translate("MainWindow", u"https://mutagen.readthedocs.io/en/latest/", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.mutagenBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.mutagenBtn.setText(QCoreApplication.translate("MainWindow", u"mutagen", None))
#if QT_CONFIG(tooltip)
        self.githubBtn.setToolTip(QCoreApplication.translate("MainWindow", u"https://github.com/RomaP13/RhythmRider", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.githubBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.githubBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.githubBtn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

