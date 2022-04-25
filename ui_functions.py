from main import *
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



class UIFunctions(MainWindow):
    

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 64

            # SET MAX WIDTH
            if width == 64:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def currentButton(self, currentIndex, enable):
        index = currentIndex
        btn_style_normal = """
        QPushButton{
	        text-align: left;
	        padding-left:22px;
	        border: 0px solid;
        }
        QPushButton:hover {
	        background-color: rgb(200, 200, 200);
        }
        QPushButton:pressed {
	        background-color: rgb(100, 100, 200);
        }
        QPushButton[color = "0"]{
            background-color: #92B4E2;
        }
        """
        btn_style_choosen = """
        QPushButton{
            background-color: #92B4E2;
	        text-align: left;
	        padding-left:22px;
	        border: 0px solid;
        }
        QPushButton:hover {
	        background-color: rgb(200, 200, 200);
        }
        QPushButton:pressed {
	        background-color: rgb(100, 100, 200);
        }
        """
        if enable:
            if index == 0:
                self.ui.Btn_home.setStyleSheet(btn_style_choosen)
                self.ui.Btn_statistic.setStyleSheet(btn_style_normal)
                self.ui.Btn_data.setStyleSheet(btn_style_normal)
                self.ui.Btn_news.setStyleSheet(btn_style_normal)
            elif index == 1:
                self.ui.Btn_home.setStyleSheet(btn_style_normal)
                self.ui.Btn_statistic.setStyleSheet(btn_style_choosen)
                self.ui.Btn_data.setStyleSheet(btn_style_normal)
                self.ui.Btn_news.setStyleSheet(btn_style_normal)
            elif index == 2:
                self.ui.Btn_home.setStyleSheet(btn_style_normal)
                self.ui.Btn_statistic.setStyleSheet(btn_style_normal)
                self.ui.Btn_data.setStyleSheet(btn_style_choosen)
                self.ui.Btn_news.setStyleSheet(btn_style_normal)
            elif index == 3:
                self.ui.Btn_home.setStyleSheet(btn_style_normal)
                self.ui.Btn_statistic.setStyleSheet(btn_style_normal)
                self.ui.Btn_data.setStyleSheet(btn_style_normal)
                self.ui.Btn_news.setStyleSheet(btn_style_choosen)
            

