# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# Author: Damilola Olawoyin-Yussuf


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

import register


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.statusbar = QtWidgets.QStatusBar(self)
        self.menubar = QtWidgets.QMenuBar(self)
        self.centralwidget = QtWidgets.QWidget(self)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.direction = QtWidgets.QLabel(self.centralwidget)
        self.btRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btRecord = QtWidgets.QPushButton(self.centralwidget)
        self.setWindowIcon(QtGui.QIcon('Icon.png'))

        self.registerWindow = register.RegisterWindow()

    def setupUi(self):
        cen = Qt.AlignmentFlag.AlignHCenter
        self.setObjectName("MainWindow")
        self.setFixedSize(800, 500)
        # self.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        self.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.logo.setGeometry(QtCore.QRect(300, 110, 193, 56))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("EPFL Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.title.setGeometry(QtCore.QRect(20, 200, 751, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        # font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.title.setStyleSheet("color: #52575C; ")

        self.direction.setGeometry(QtCore.QRect(10, 250, 781, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.direction.setFont(font)
        self.direction.setScaledContents(True)
        self.direction.setWordWrap(True)
        # self.direction.adjustSize()
        self.direction.setObjectName("direction")
        self.direction.setStyleSheet("color: #52575C; ")

        self.logo.setAlignment(cen)
        self.title.setAlignment(cen)
        self.direction.setAlignment(cen)

        self.btRegister.setGeometry(QtCore.QRect(180, 350, 136, 42))
        self.btRegister.setStyleSheet("border-radius: 4px; "
                                      "color: white; "
                                      "background-color : #005FB8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btRegister.setFont(font)
        self.btRegister.setObjectName("btRegister")
        self.btRegister.clicked.connect(self.launchRegisterSession)

        self.btRecord.setGeometry(QtCore.QRect(480, 350, 136, 42))
        self.btRecord.setStyleSheet("border-radius: 4px; "
                                    "color: white; "
                                    "background-color : #005FB8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btRecord.setFont(font)
        self.btRecord.setObjectName("btRecord")

        self.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 51))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "EPFL Smart Kitchen Recorder"))
        self.title.setText(_translate("MainWindow", "Welcome to the EPFL Smart Kitchen Recorder"))
        self.direction.setText(_translate("MainWindow", "Please click on one of the buttons to either register a "
                                                        "subject or record a session"))
        self.btRegister.setText(_translate("MainWindow", "Register Subject"))
        self.btRecord.setText(_translate("MainWindow", "Record Session"))

    def launchRegisterSession(self):
        self.close()
        self.registerWindow.setupUi()
        self.registerWindow.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # mainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
