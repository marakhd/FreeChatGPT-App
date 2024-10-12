from PyQt5 import QtCore, QtGui, QtWidgets
from .text_edit import EnterTextEdit
from .rcc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 676)
        MainWindow.setMinimumSize(QtCore.QSize(450, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1080))
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"background-image: url(:/bg/bg.webp);\n"
"background-repeat: no-repeat; /* Избегаем повторений */\n"
"background-position: center; /* Центрируем изображение */\n"
"}\n"
"QListWidget#chatListWidget {\n"
"background-color: rgba(255, 255, 255, .8);\n"
"border-radius: 12px;\n"
"padding: 10px;\n"
"}\n"
"* {\n"
"font-family: \"JetBrains Mono\", sans-serif;\n"
"margin: 0;\n"
"padding: 0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QHBoxLayout()
        self.header.setObjectName("header")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem)
        self.headerText = QtWidgets.QLabel(self.centralwidget)
        self.headerText.setStyleSheet("font-weight: bold;\n"
"font: 25px \"JetBrains Mono\";")
        self.headerText.setObjectName("headerText")
        self.header.addWidget(self.headerText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.header)
        self.chatLayout = QtWidgets.QHBoxLayout()
        self.chatLayout.setSpacing(0)
        self.chatLayout.setObjectName("chatLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.chatLayout.addItem(spacerItem2)
        self.chatListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.chatListWidget.setObjectName("chatListWidget")
        self.chatLayout.addWidget(self.chatListWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.chatLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.chatLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setObjectName("bottomLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem5)
        self.fieldWidget = QtWidgets.QWidget(self.centralwidget)
        self.fieldWidget.setMaximumSize(QtCore.QSize(450, 120))
        self.fieldWidget.setStyleSheet("#fieldWidget {\n"
"background-color: rgba(255, 255, 255, .8);\n"
"border-radius: 12px;\n"
"padding: 0;\n"
"}\n"
"QPushButton#sendButton {\n"
"margin: 5px;\n"
"background-color: rgba(255, 255, 255, .0);\n"
"border: 2px solid black;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton#sendButton:pressed {\n"
"background-color: rgba(0, 0, 0, .6);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgba(255, 255, 255, .0);\n"
"border-radius: 12px;\n"
"padding: 5px;\n"
"}")
        self.fieldWidget.setObjectName("fieldWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fieldWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnWidget = QtWidgets.QWidget(self.fieldWidget)
        self.sendButton = QtWidgets.QPushButton(self.btnWidget)
        self.inputField = EnterTextEdit(self.fieldWidget, self.sendButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputField.sizePolicy().hasHeightForWidth())
        self.inputField.setSizePolicy(sizePolicy)
        self.inputField.setMinimumSize(QtCore.QSize(350, 0))
        self.inputField.setMaximumSize(QtCore.QSize(16777215, 124))
        self.inputField.setStyleSheet("")
        self.inputField.setObjectName("inputField")
        self.horizontalLayout.addWidget(self.inputField)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btnWidget.setMinimumSize(QtCore.QSize(0, 120))
        self.btnWidget.setStyleSheet("")
        self.btnWidget.setObjectName("btnWidget")
        self.btnLayout = QtWidgets.QVBoxLayout(self.btnWidget)
        self.btnLayout.setObjectName("btnLayout")
        spacerItem7 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnLayout.addItem(spacerItem7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QtCore.QSize(60, 60))
        self.sendButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon-send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon)
        self.sendButton.setObjectName("sendButton")
        self.btnLayout.addWidget(self.sendButton)
        self.horizontalLayout.addWidget(self.btnWidget)
        self.bottomLayout.addWidget(self.fieldWidget)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.bottomLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menuBar.setAcceptDrops(False)
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setAcceptDrops(False)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.offBtnSend = QtWidgets.QAction(MainWindow)
        self.offBtnSend.setCheckable(True)
        self.offBtnSend.setObjectName("offBtnSend")
        self.clearCtx = QtWidgets.QAction(MainWindow)
        self.clearCtx.setObjectName("clearCtx")
        self.menu.addAction(self.offBtnSend)
        self.menu.addSeparator()
        self.menu.addAction(self.clearCtx)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerText.setText(_translate("MainWindow", "ChatGPT"))
        self.inputField.setPlaceholderText(_translate("MainWindow", "Введите запрос..."))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.offBtnSend.setText(_translate("MainWindow", "Отключить кнопку отправки"))
        self.offBtnSend.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.clearCtx.setText(_translate("MainWindow", "Очистить контекст"))
        self.clearCtx.setShortcut(_translate("MainWindow", "Ctrl+R"))
