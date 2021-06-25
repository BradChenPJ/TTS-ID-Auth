# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ID_auth.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    #MainWindow會帶入QtWidgets.QMainWindow()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(550, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.company_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.company_edit.setGeometry(QtCore.QRect(145, 45, 341, 31))
        self.company_edit.setObjectName("company_edit")
        self.company = QtWidgets.QLabel(self.centralwidget)
        self.company.setGeometry(QtCore.QRect(64, 35, 81, 51))
        self.company.setTextFormat(QtCore.Qt.AutoText)
        self.company.setScaledContents(True)
        self.company.setObjectName("company")
        self.company.setTextInteractionFlags(Qt.TextSelectableByMouse)   #讓label可以被滑鼠選擇並複製
        self.man = QtWidgets.QLabel(self.centralwidget)
        self.man.setGeometry(QtCore.QRect(64, 111, 81, 51))
        self.man.setTextFormat(QtCore.Qt.AutoText)
        self.man.setScaledContents(True)
        self.man.setObjectName("man")
        self.contact = QtWidgets.QLabel(self.centralwidget)
        self.contact.setGeometry(QtCore.QRect(64, 187, 81, 51))
        self.contact.setTextFormat(QtCore.Qt.AutoText)
        self.contact.setScaledContents(True)
        self.contact.setObjectName("contact")
        self.man_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.man_edit.setGeometry(QtCore.QRect(145, 121, 341, 31))
        self.man_edit.setObjectName("man_edit")
        self.contact_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.contact_edit.setGeometry(QtCore.QRect(145, 197, 341, 31))
        self.contact_edit.setObjectName("contact_edit")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(390, 260, 101, 31))
        self.ok_button.setObjectName("ok_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.company.setText(_translate("MainWindow", "公司名稱："))
        self.man.setText(_translate("MainWindow", "聯絡人："))
        self.contact.setText(_translate("MainWindow", "聯絡方式："))
        self.ok_button.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

