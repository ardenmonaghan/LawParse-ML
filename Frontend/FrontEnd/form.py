# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 713)
        MainWindow.setStyleSheet(u"#new_chat_frame QPushButton {\n"
"text-align: left;\n"
"}\n"
"\n"
"#menu_frame QPushButton {\n"
"color: #fff;\n"
"border: none;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background: none;\n"
"}\n"
"\n"
"#menu_frame {\n"
"border-top: 0.5px solid #fff;\n"
"}\n"
"\n"
"#menu_frame QFrame {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#new_chat_btn {\n"
"border: 1px solid #4d4d4f;\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"}\n"
"\n"
"#side_widget, \n"
"#chat_list {\n"
"background: #282828;\n"
"}\n"
"\n"
"#chat_list {\n"
"border: none;\n"
"}\n"
"\n"
"#chat_list_frame {\n"
"border: none;\n"
"}\n"
"\n"
"#side_widget QPushButton:hover, \n"
"#chat_list:item_hover,\n"
"#user_frame:hover,\n"
"#menu_frame QFrame:hover {\n"
"background: #2a2b32;\n"
"}\n"
"\n"
"#comboBox {\n"
"border: none;\n"
"background: transparent;\n"
"color: #fff;\n"
"padding: 10px;\n"
"}\n"
"\n"
"#input_frame {\n"
"border: 1px solid #e5e5e5;\n"
"background: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#input_textEdit {\n"
"border: n"
                        "one;\n"
"background: #fff;\n"
"}\n"
"\n"
"#send_btn {\n"
"border: none;\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#send_btn:hover {\n"
"background: #ececf1;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.side_widget = QWidget(self.centralwidget)
        self.side_widget.setObjectName(u"side_widget")
        self.side_widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.side_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.new_chat_frame = QFrame(self.side_widget)
        self.new_chat_frame.setObjectName(u"new_chat_frame")
        self.new_chat_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.new_chat_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.new_chat_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.new_chat_btn = QPushButton(self.new_chat_frame)
        self.new_chat_btn.setObjectName(u"new_chat_btn")
        self.new_chat_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.new_chat_btn)


        self.verticalLayout_2.addWidget(self.new_chat_frame)

        self.chat_list_frame = QFrame(self.side_widget)
        self.chat_list_frame.setObjectName(u"chat_list_frame")
        self.chat_list_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chat_list_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.chat_list_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chat_list = QListView(self.chat_list_frame)
        self.chat_list.setObjectName(u"chat_list")

        self.gridLayout.addWidget(self.chat_list, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.chat_list_frame)

        self.menu_frame = QFrame(self.side_widget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font = QFont()
        font.setFamilies([u"Sathu"])
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_4.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.menu_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.menu_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 8, -1, 8)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.menu_frame)


        self.horizontalLayout_6.addWidget(self.side_widget)

        self.main_window = QWidget(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.gridLayout_4 = QGridLayout(self.main_window)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 20)
        self.input_frame = QFrame(self.main_window)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setMaximumSize(QSize(650, 100))
        self.input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.input_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(12, 12, 7, 15)
        self.send_btn = QPushButton(self.input_frame)
        self.send_btn.setObjectName(u"send_btn")

        self.gridLayout_2.addWidget(self.send_btn, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.input_textEdit = QTextEdit(self.input_frame)
        self.input_textEdit.setObjectName(u"input_textEdit")
        self.input_textEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.input_textEdit, 0, 0, 2, 1)


        self.gridLayout_4.addWidget(self.input_frame, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.main_window)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 749, 567))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 540, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.main_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1001, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.new_chat_btn.setText(QCoreApplication.translate("MainWindow", u"New Chat", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VR", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Document Retrieval", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VR", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Version Control", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VR", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Llama3", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VR", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear All Conversations", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

