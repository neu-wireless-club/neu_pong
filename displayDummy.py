from PyQt4 import QtGui,QtCore,Qt
import sys
import time


class Pixel(QtGui.QTableWidgetItem):
    def __init__(self):
        super(Pixel, self).__init__()
        self.setBackgroundColor(QtCore.Qt.black)

    def setState(self,state):
        print 'yo'
        if state:
            self.setBackgroundColor(QtCore.Qt.red)
        else:
            self.setBackgroundColor(QtCore.Qt.black)

class GameDisplay(QtGui.QWidget):
    def __init__(self,numCols=10,numRows=10,cellHeight=20,cellWidth=20):
        super(GameDisplay, self).__init__()
        self.numCols = numCols
        self.numRows = numRows
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.cellWidth*self.numCols+50, self.cellHeight*self.numRows+50)
        self.setWindowTitle('Game')

        self.grid = QtGui.QTableWidget()
        self.grid.setColumnCount(self.numCols)
        self.grid.setRowCount(self.numRows)
        self.grid.horizontalHeader().setDefaultSectionSize(self.cellWidth)
        self.grid.verticalHeader().setDefaultSectionSize(self.cellHeight)
        self.grid.horizontalHeader().setResizeMode(2)
        self.grid.verticalHeader().setResizeMode(2)
        for i in range(self.numRows):
            for j in range(self.numCols):
                tmp = Pixel()
                self.grid.setItem(i,j,tmp)
        self.lay = QtGui.QHBoxLayout()
        self.lay.addWidget(self.grid)
        self.setLayout(self.lay)

        self.show()

    def displayPoint(self,pointX,pointY,setTo) :
        pointY-=1
        pointX-=1
        pxl = self.grid.item(pointX,pointY)
        pxl.setState(setTo)



def main():
    app = QtGui.QApplication(sys.argv)
    gui = GameDisplay()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()