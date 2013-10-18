__author__ = 'bryce'

from PyQt4 import QtGui,QtCore,Qt
import sys

class Pixel(QtGui.QWidget):
    def __init__(self):
        super(Pixel, self).__init__()
        self.setFixedHeight(50)
        self.setFixedWidth(50)
        self.p = QtGui.QPalette()
        self.p.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(self.p)

    def setState(self,state):
        if state == True:
            self.p.setColor(QtGui.QPalette.Background, QtCore.Qt.red)
        else:
            self.p.setColor(QtGui.QPalette.Background, QtCore.Qt.black)

class GameDisplay(QtGui.QWidget):
    def __init__(self):
        super(GameDisplay, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Game')

        self.grid = QtGui.QGridLayout()

        for i in range(10):
            for j in range(10):
                tmp = Pixel()
                self.grid.addWidget(tmp,i,j)

        self.setLayout(self.grid)

        self.show()

    def displayPoint(self,pointX,pointY,setTo):
        pxl = self.grid.itemAtPosition(pointX,pointY)
        pxl.setState(setTo)



def main():
    app = QtGui.QApplication(sys.argv)
    gui = GameDisplay()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()