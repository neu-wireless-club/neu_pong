from PyQt4 import QtGui,QtCore,Qt
import sys


class Pixel(QtGui.QTableWidgetItem):
    def __init__(self):
        super(Pixel, self).__init__()
        self.setBackgroundColor(QtCore.Qt.black)

    def setState(self,state):
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

        self.pointPos = [1,1]

        self.grid = QtGui.QTableWidget()
        self.grid.setColumnCount(self.numCols)
        self.grid.setRowCount(self.numRows)
        self.grid.horizontalHeader().setDefaultSectionSize(self.cellWidth)
        self.grid.verticalHeader().setDefaultSectionSize(self.cellHeight)
        self.grid.horizontalHeader().setResizeMode(2)
        self.grid.verticalHeader().setResizeMode(2)
        self.grid.setEnabled(False)
        for i in range(self.numRows):
            for j in range(self.numCols):
                tmp = Pixel()
                self.grid.setItem(i,j,tmp)
        self.lay = QtGui.QHBoxLayout()
        self.lay.addWidget(self.grid)
        self.setLayout(self.lay)

        self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        self.show()


    def displayPoint(self,pointX,pointY,setTo) :
        pointY-=1
        pointX-=1
        pxl = self.grid.item(pointY,pointX)
        pxl.setState(setTo)

    def movePoint(self,dir):
        print dir
        if dir == 'up':
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[1] = self.pointPos[1]-1 if self.pointPos[1]>1 else 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'down':
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[1] = self.pointPos[1]+1 if self.pointPos[1]<self.numRows else self.numRows
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'left':
            print 'left'
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[0] = self.pointPos[0]-1 if self.pointPos[0]>1 else 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'right':
            print 'right'
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[0] = self.pointPos[0]+1 if self.pointPos[0]<self.numCols else self.numCols
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)

    def keyPressEvent(self, e):
        print 'hi'
        if e.key() == QtCore.Qt.Key_Up:
            self.movePoint('up')
        if e.key() == QtCore.Qt.Key_Down:
            self.movePoint('down')
        if e.key() == QtCore.Qt.Key_Left:
            self.movePoint('left')
        if e.key() == QtCore.Qt.Key_Right:
            self.movePoint('right')
def main():
    app = QtGui.QApplication(sys.argv)
    gui = GameDisplay()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()