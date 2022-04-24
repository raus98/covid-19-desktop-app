# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainNwBAoG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 945)
        MainWindow.setMinimumSize(QSize(1440, 945))
        MainWindow.setMaximumSize(QSize(1440, 945))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 72))
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(64, 72))
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"border: 0px solid\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(32, 46))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_name = QFrame(self.frame_top)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setGeometry(QRect(1193, 0, 80, 72))
        self.frame_name.setMaximumSize(QSize(100, 72))
        self.frame_name.setFrameShape(QFrame.StyledPanel)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.user_name = QLabel(self.frame_name)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(0, 30, 80, 13))
        self.user_name.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_name.setFont(font)
        self.frame_avatar = QFrame(self.frame_top)
        self.frame_avatar.setObjectName(u"frame_avatar")
        self.frame_avatar.setGeometry(QRect(1287, 0, 88, 72))
        self.frame_avatar.setMaximumSize(QSize(88, 72))
        self.frame_avatar.setFrameShape(QFrame.StyledPanel)
        self.frame_avatar.setFrameShadow(QFrame.Raised)
        self.frame_avatar.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_avatar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 2, 0)
        self.avatar = QLabel(self.frame_avatar)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMaximumSize(QSize(40, 40))
        self.avatar.setFocusPolicy(Qt.StrongFocus)
        self.avatar.setLineWidth(0)
        self.avatar.setPixmap(QPixmap(u"icon/avatar.png"))
        self.avatar.setAlignment(Qt.AlignCenter)
        self.avatar.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_5.addWidget(self.avatar)

        self.frame_bell = QFrame(self.frame_top)
        self.frame_bell.setObjectName(u"frame_bell")
        self.frame_bell.setGeometry(QRect(1100, 0, 35, 72))
        self.frame_bell.setMaximumSize(QSize(35, 72))
        self.frame_bell.setFrameShape(QFrame.StyledPanel)
        self.frame_bell.setFrameShadow(QFrame.Raised)
        self.bell = QLabel(self.frame_bell)
        self.bell.setObjectName(u"bell")
        self.bell.setGeometry(QRect(0, 28, 15, 16))
        self.bell.setMaximumSize(QSize(15, 16))
        self.bell.setPixmap(QPixmap(u"icon/bell.png"))
        self.bell.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_line = QFrame(self.frame_top)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setGeometry(QRect(1115, 0, 47, 72))
        self.frame_line.setMaximumSize(QSize(50, 72))
        self.frame_line.setFrameShape(QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QFrame.Raised)
        self.line = QLabel(self.frame_line)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 16, 47, 40))
        self.line.setPixmap(QPixmap(u"icon/line.png"))
        self.line.setAlignment(Qt.AlignCenter)
        self.line.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(64, 0))
        self.frame_left_menu.setMaximumSize(QSize(64, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Menu_1 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setObjectName(u"Btn_Menu_1")
        self.Btn_Menu_1.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_1)

        self.Btn_Menu_2 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setObjectName(u"Btn_Menu_2")
        self.Btn_Menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_2)

        self.Btn_Menu_3 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setObjectName(u"Btn_Menu_3")
        self.Btn_Menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.Pages_Widget.setGeometry(QRect(10, 10, 1361, 861))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Pages_Widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Pages_Widget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.avatar.setText("")
        self.bell.setText("")
        self.line.setText("")
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"Menu 1", None))
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"Menu 1", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"Menu 1", None))
    # retranslateUi

