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
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPlainTextEdit,
)


def fontOnly(fontFamily: str, pointSize: int, bold=False):
    font = QtGui.QFont()
    font.setFamily(fontFamily)
    font.setBold(bold)
    font.setPointSize(pointSize)
    return font


class RecordWindow(QMainWindow):
    def __init__(self):
        super(RecordWindow, self).__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.statusbar = QtWidgets.QStatusBar(self)
        self.menubar = QtWidgets.QMenuBar(self)
        self.centralwidget = QtWidgets.QWidget(self)
        self.title = self.labelOnly(20, 25, 300, 41, "Record Session", "title", 12)
        self.logo = QtWidgets.QLabel(self.centralwidget)

        self.cSubjectLabel, self.cSubjectEdit = self.labelEditCombo(20, 90, 140, 20, "Choose Subject:", "cSubjectLabel",
                                                                    "cSubjectEdit")
        self.sLengthLabel, self.sLengthEdit = self.labelEditCombo(20, 150, 230, 20, "Session Length (in seconds):",
                                                                  "sLengthLabel", "sLengthEdit")
        self.commentLabel, self.commentEdit = self.plainEditCombo(20, 210, 100, 20,  "Comments:",
                                                                  "commentLabel", "commentEdit")
        self.btRecord = self.buttonOnly(120, 350, 160, 42, "Start Recording", "btRecord", "#005FB8", 10)
        self.btEnd = self.buttonOnly(350, 350, 150, 42, "End Session", "btEnd", "#B80000", 10)

        # self.mainWindow = MyMainWindow()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.setFixedSize(800, 560)
        self.setFont(fontOnly("Bookman Old Style", 22))
        self.centralwidget.setObjectName("centralwidget")
        self.logo.setGeometry(QtCore.QRect(670, 20, 115, 33))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("EPFL Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.title.setScaledContents(True)
        self.title.setWordWrap(True)

        self.btRecord.clicked.connect(self.launchMainSession)

        self.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 51))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(self._translate("MainWindow", "EPFL Smart Kitchen Recorder"))

    def launchMainSession(self):
        self.close()
        # self.mainWindow.show()

    def labelEditCombo(self, xpos, ypos, width, height, labelName: str, labelObjectName: str, editObjectName: str):
        label = self.labelOnly(xpos, ypos, width, height, labelName, labelObjectName, 10)

        edit = QLineEdit(self.centralwidget)
        edit.setGeometry(QtCore.QRect(xpos + width, ypos, width + 100, height + 10))
        edit.setFont(fontOnly("Segoe UI", 10))
        edit.setObjectName(editObjectName)
        edit.setStyleSheet("color: #52575C; ")
        return label, edit

    def labelOnly(self, xpos, ypos, width, height, labelName: str, labelObjectName: str, pointSize: int):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(xpos, ypos, width, height))
        label.setFont(fontOnly("Segoe UI", pointSize))
        label.setObjectName(labelObjectName)
        label.setStyleSheet("color: #52575C; ")
        label.setText(self._translate("MainWindow", labelName))
        return label

    def buttonOnly(self, xpos, ypos, width, height, btName: str, btObjectName: str, background: str, fontSize: int):
        button = QtWidgets.QPushButton(self.centralwidget)
        button.setGeometry(QtCore.QRect(xpos, ypos, width, height))
        button.setFont(fontOnly("Arial", fontSize))
        button.setObjectName(btObjectName)
        button.setStyleSheet("border-radius: 4px; "
                             "color: white; "
                             "background-color : " + background)
        button.setText(self._translate("MainWindow", btName))
        return button

    def plainEditCombo(self, xpos, ypos, width, height, labelName: str, labelObjectName: str, editObjectName: str):
        label = self.labelOnly(xpos, ypos, width, height, labelName, labelObjectName, 10)

        edit = QPlainTextEdit(self.centralwidget)
        edit.setGeometry(QtCore.QRect(xpos + width, ypos, width + 300, height + 60))
        edit.setFont(fontOnly("Segoe UI", 10))
        edit.setObjectName(editObjectName)
        edit.setStyleSheet("color: #52575C; ")
        return label, edit


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = RecordWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
