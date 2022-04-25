
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
            
        ## TOGGLE BUTTON
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        ## PAGES
        self.ui.Btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_home))
        self.ui.Btn_statistic.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_statistic))
        self.ui.Btn_data.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_data))
        self.ui.Btn_news.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_news))

        ## GET CURRENT WIDGET
        self.ui.Btn_home.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.Btn_statistic.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.Btn_data.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
        self.ui.Btn_news.clicked.connect(lambda: UIFunctions.currentButton(self, self.ui.stackedWidget.currentIndex(),True))
           

        ## SHOW ==> MAIN WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())