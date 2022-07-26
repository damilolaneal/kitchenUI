from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        xpos = 100
        ypos = 100
        width = 300
        height = 300
        self.btRecord = QtWidgets.QPushButton(self)
        self.btRegister = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("EPFL Smart Kitchen Recorder")
        self.initUI()

    def initUI(self):
        self.label.setText("Welcome to the EPFL Smart Kitchen Recorder")
        self.label.move(50, 50)

        self.btRegister.setText("Register Subject")
        self.btRegister.clicked.connect(self.clickRegister)

        self.btRecord.setText("Record Session")

    @pyqtSlot()
    def clickRegister(self):
        self.label.setText("You want to Register")
        self.update()
        return True

    def update(self) -> None:
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
