# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainIeFeCe.ui'
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
        self.Top_Bar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(64, 72))
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.frame_toggle.setLineWidth(0)
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

        self.frame_user = QFrame(self.Top_Bar)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.frame_user.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_bell = QFrame(self.frame_user)
        self.frame_bell.setObjectName(u"frame_bell")
        self.frame_bell.setLayoutDirection(Qt.RightToLeft)
        self.frame_bell.setFrameShape(QFrame.NoFrame)
        self.frame_bell.setFrameShadow(QFrame.Raised)
        self.frame_bell.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_bell)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 22, 0)
        self.bell = QLabel(self.frame_bell)
        self.bell.setObjectName(u"bell")
        self.bell.setMinimumSize(QSize(16, 16))
        self.bell.setPixmap(QPixmap(u"icon/bell.png"))

        self.horizontalLayout_6.addWidget(self.bell)


        self.horizontalLayout_3.addWidget(self.frame_bell)

        self.frame_line = QFrame(self.frame_user)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setLayoutDirection(Qt.RightToLeft)
        self.frame_line.setFrameShape(QFrame.NoFrame)
        self.frame_line.setFrameShadow(QFrame.Raised)
        self.frame_line.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_line)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 54, 0)
        self.line = QLabel(self.frame_line)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 40))
        self.line.setLayoutDirection(Qt.RightToLeft)
        self.line.setLineWidth(0)
        self.line.setPixmap(QPixmap(u"icon/line.png"))

        self.horizontalLayout_7.addWidget(self.line)


        self.horizontalLayout_3.addWidget(self.frame_line)

        self.frame_name = QFrame(self.frame_user)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.frame_name.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 22, 0)
        self.name = QLabel(self.frame_name)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.name)


        self.horizontalLayout_3.addWidget(self.frame_name, 0, Qt.AlignRight)

        self.frame_avatar = QFrame(self.frame_user)
        self.frame_avatar.setObjectName(u"frame_avatar")
        self.frame_avatar.setFrameShape(QFrame.StyledPanel)
        self.frame_avatar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_avatar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 48, 0)
        self.avatar_button = QToolButton(self.frame_avatar)
        self.avatar_button.setObjectName(u"avatar_button")
        self.avatar_button.setMinimumSize(QSize(40, 40))
        self.avatar_button.setStyleSheet(u"QToolButton{\n"
"	border: 0px solid;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/avatar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.avatar_button.setIcon(icon1)
        self.avatar_button.setIconSize(QSize(40, 40))
        self.avatar_button.setArrowType(Qt.NoArrow)

        self.horizontalLayout_4.addWidget(self.avatar_button)


        self.horizontalLayout_3.addWidget(self.frame_avatar, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_user, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.Content.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMaximumSize(QSize(64, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_left_menu.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.frame_top_menus.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_home = QPushButton(self.frame_top_menus)
        self.Btn_home.setObjectName(u"Btn_home")
        self.Btn_home.setMinimumSize(QSize(0, 64))
        self.Btn_home.setMaximumSize(QSize(200, 16777215))
        self.Btn_home.setFont(font)
        self.Btn_home.setStyleSheet(u"QPushButton{\n"
"	background-color: #92B4E2;\n"
"	text-align: left;\n"
"	padding-left:22px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 200);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_home.setIcon(icon2)
        self.Btn_home.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_home)

        self.Btn_statistic = QPushButton(self.frame_top_menus)
        self.Btn_statistic.setObjectName(u"Btn_statistic")
        self.Btn_statistic.setMinimumSize(QSize(0, 64))
        self.Btn_statistic.setMaximumSize(QSize(200, 16777215))
        self.Btn_statistic.setFont(font)
        self.Btn_statistic.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:22px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 200);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icon/statistic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_statistic.setIcon(icon3)
        self.Btn_statistic.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_statistic)

        self.Btn_data = QPushButton(self.frame_top_menus)
        self.Btn_data.setObjectName(u"Btn_data")
        self.Btn_data.setMinimumSize(QSize(0, 64))
        self.Btn_data.setMaximumSize(QSize(200, 16777215))
        self.Btn_data.setFont(font)
        self.Btn_data.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:22px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 200);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icon/data.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_data.setIcon(icon4)
        self.Btn_data.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_data)

        self.Btn_news = QPushButton(self.frame_top_menus)
        self.Btn_news.setObjectName(u"Btn_news")
        self.Btn_news.setMinimumSize(QSize(0, 64))
        self.Btn_news.setMaximumSize(QSize(200, 16777215))
        self.Btn_news.setFont(font)
        self.Btn_news.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:22px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 200);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icon/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_news.setIcon(icon5)
        self.Btn_news.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_news)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.frame_pages.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.frame_home = QWidget()
        self.frame_home.setObjectName(u"frame_home")
        self.verticalLayout_7 = QVBoxLayout(self.frame_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_home = QLabel(self.frame_home)
        self.lb_home.setObjectName(u"lb_home")
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setWeight(50)
        self.lb_home.setFont(font1)
        self.lb_home.setLineWidth(0)
        self.lb_home.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_home)

        self.stackedWidget.addWidget(self.frame_home)
        self.frame_statistic = QWidget()
        self.frame_statistic.setObjectName(u"frame_statistic")
        self.verticalLayout_8 = QVBoxLayout(self.frame_statistic)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lb_statistic = QLabel(self.frame_statistic)
        self.lb_statistic.setObjectName(u"lb_statistic")
        self.lb_statistic.setFont(font1)
        self.lb_statistic.setLineWidth(0)
        self.lb_statistic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_statistic)

        self.stackedWidget.addWidget(self.frame_statistic)
        self.frame_data = QWidget()
        self.frame_data.setObjectName(u"frame_data")
        self.verticalLayout_9 = QVBoxLayout(self.frame_data)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_data = QLabel(self.frame_data)
        self.lb_data.setObjectName(u"lb_data")
        self.lb_data.setFont(font1)
        self.lb_data.setLineWidth(0)
        self.lb_data.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lb_data)

        self.stackedWidget.addWidget(self.frame_data)
        self.frame_news = QWidget()
        self.frame_news.setObjectName(u"frame_news")
        self.verticalLayout_10 = QVBoxLayout(self.frame_news)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb_news = QLabel(self.frame_news)
        self.lb_news.setObjectName(u"lb_news")
        self.lb_news.setFont(font1)
        self.lb_news.setLineWidth(0)
        self.lb_news.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lb_news)

        self.stackedWidget.addWidget(self.frame_news)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.bell.setText("")
        self.line.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.avatar_button.setText("")
        self.Btn_home.setText(QCoreApplication.translate("MainWindow", u"     Home", None))
        self.Btn_statistic.setText(QCoreApplication.translate("MainWindow", u"     Statistic", None))
        self.Btn_data.setText(QCoreApplication.translate("MainWindow", u"     Data", None))
        self.Btn_news.setText(QCoreApplication.translate("MainWindow", u"     News", None))
        self.lb_home.setText(QCoreApplication.translate("MainWindow", u"HOME PAGE", None))
        self.lb_statistic.setText(QCoreApplication.translate("MainWindow", u"STATISTIC PAGE", None))
        self.lb_data.setText(QCoreApplication.translate("MainWindow", u"DATA PAGE", None))
        self.lb_news.setText(QCoreApplication.translate("MainWindow", u"NEWS PAGE", None))
    # retranslateUi

