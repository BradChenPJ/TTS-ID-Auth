# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UUID.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import subprocess
from loadFigure import FigureSet
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def __inint__(self):
        self.OKcopy = None
    def setupUi(self, MainWindow, UUIDnum):
        #圖集
        fig = FigureSet()
        icon = QPixmap()
        icon.loadFromData(fig.icon)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 206)
        MainWindow.setWindowIcon(QtGui.QIcon(icon))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 26, 500, 41))
        self.title.setObjectName("title")
        self.title.setFont(QFont('Arial', 14))
        self.UUID = QtWidgets.QLabel(self.centralwidget)
        self.UUID.setGeometry(QtCore.QRect(10, 90, 1190, 41))
        self.UUID.setObjectName("UUID")
        self.UUID.setFont(QFont('Arial', 10))
        self.UUID.setText(UUIDnum)
        self.UUID.setTextInteractionFlags(Qt.TextSelectableByMouse)   #讓label可以被滑鼠選擇並複製
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName("menubar")
        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.copy_button.setObjectName("copy_button")
        self.copy_button.clicked.connect(lambda: self.copyText(UUIDnum))
        self.OKcopy = QtWidgets.QLabel(self.centralwidget)
        self.OKcopy.setGeometry(QtCore.QRect(130, 150, 90, 31))
        self.OKcopy.setObjectName("OKcopy")
        self.OKcopy.setFont(QFont('Arial', 12))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登錄成功"))
        self.title.setText(_translate("MainWindow", "請聯繫業務並告知以下密碼："))
        self.copy_button.setText(_translate("MainWindow", "一鍵複製"))
    def copyText(self,UUIDnum):
        try:
            subprocess.run(['clip.exe'], input=UUIDnum.strip().encode('utf-16'), check=True)
            self.OKcopy.setText("OK！")
        except:
            pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

