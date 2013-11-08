import copy
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
# "global" variables used to move the pointer with timer
# set default values first
    pointX = 0 
    pointY = 0
    xMax = 9
    yMax = 9
    moveDirX = 'none'
    moveDirY = 'none'

    def __init__(self,numCols=10,numRows=10,cellHeight=20,cellWidth=20):
        super(GameDisplay, self).__init__()
        self.numCols = numCols
        self.numRows = numRows
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.pointPos = [1,1]
        self.moveDir = [1,0]
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.cellWidth*self.numCols+50, self.cellHeight*self.numRows+50)
        self.setWindowTitle('Game')

        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(self.numCols)
        self.table.setRowCount(self.numRows)
        self.table.horizontalHeader().setDefaultSectionSize(self.cellWidth)
        self.table.verticalHeader().setDefaultSectionSize(self.cellHeight)
        self.table.horizontalHeader().setResizeMode(2)
        self.table.verticalHeader().setResizeMode(2)
        self.table.setEnabled(False)
        for i in range(self.numRows):
            for j in range(self.numCols):
                tmp = Pixel()
                self.table.setItem(i,j,tmp)

        self.lay = QtGui.QHBoxLayout()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)

        self.displayPoint(self.pointPos[0],self.pointPos[1],True)

        self.bTimer = QtCore.QBasicTimer()
        self.bTimer.start(100,self)

        self.show()


    def displayPoint(self,pointX,pointY,setTo) :
        pointY-=1
        pointX-=1
        pxl = self.table.item(pointY,pointX)
        pxl.setState(setTo)

    def movePoint(self,dir):
#        print dir
        lastPos = copy.deepcopy(self.pointPos)
        if dir == 'up':
	    self.pointY = self.pointY - 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[1] = self.pointPos[1]-1 if self.pointPos[1]>1 else 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'down':
	    self.pointY = self.pointY + 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[1] = self.pointPos[1]+1 if self.pointPos[1]<self.numRows else self.numRows
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'left':
#            print 'left'
	    self.pointX = self.pointX - 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[0] = self.pointPos[0]-1 if self.pointPos[0]>1 else 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if dir == 'right':
#            print 'right'
	    self.pointX = self.pointX + 1
            self.displayPoint(self.pointPos[0],self.pointPos[1],False)
            self.pointPos[0] = self.pointPos[0]+1 if self.pointPos[0]<self.numCols else self.numCols
            self.displayPoint(self.pointPos[0],self.pointPos[1],True)
        if lastPos == self.pointPos:
            return True
        else:
            return False

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

    def timerEvent(self,e):
	#we want to do a figure 8 kind of thing
	#check the position of the pointer, particularly at the corners
	if self.pointX == 0:
		#top left corner, move it down
		if self.pointY == 0:
			self.moveDirX = 'none'
			self.moveDirY = 'down'
		#bottom left corner, move it diagonal to the right
		if self.pointY == self.yMax:
			self.moveDirX = 'right'
			self.moveDirY = 'up'
	elif self.pointX == self.xMax:
		#top right, move it down
		if self.pointY == 0:
			self.moveDirX = 'none'
			self.moveDirY = 'down'
		#bottom right, move it diagonal to the left
		if self.pointY == self.yMax:
			self.moveDirX = 'left'
			self.moveDirY = 'up'
	#call the move method to move pointer
	self.movePoint(self.moveDirX)
	self.movePoint(self.moveDirY)
	#print position for debugging
	print str(self.pointX) + ", " + str(self.pointY)


def main():
    app = QtGui.QApplication(sys.argv)
    gui = GameDisplay()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
