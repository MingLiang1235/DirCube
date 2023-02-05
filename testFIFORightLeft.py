#coding:utf-8

import StackWithPoint

class myTestFIFOWithPoint(object):
	def testFIFOWithPoint(self):
		print "Now init fifo:"
		ls = [1,2,3]
		self.fifo = StackWithPoint.FIFOWithPoint(ls);
		print "Fifo fill with [1,2,3]."
		print "After init fifo:"
		print self.fifo
		print "The point is:" + str(self.fifo.getPoint())
		print "Push(6) is:" + str(self.fifo.push(6))
		
		print "The current is :" + str(self.fifo.getCurr())
		print "The left is :" +str(self.fifo.getLeft())
		print "The left is :" + str(self.fifo.getLeft())
		print "The left is :" + str(self.fifo.getLeft())
		print "The point is:" + str(self.fifo.getPoint())
		print "The current is :" + str(self.fifo.getCurr())
		print "The Right is :" +str(self.fifo.getRight())
		print "The point is :" + str(self.fifo.getPoint())
		print "The update(5) is:" + str(self.fifo.update(5))
		print "The current is:" + str(self.fifo.getCurr())
		print "The Point is:" + str(self.fifo.getPoint())
		print "The Right is :" + str(self.fifo.getRight())
		print "The Right is :" + str(self.fifo.getRight())
		print "The Right is :" + str(self.fifo.getRight())
		print "The point is:" + str(self.fifo.getPoint())
		print "The Left is :" + str(self.fifo.getLeft())
		print "The hole list is:"
		print self.fifo
if __name__ == '__main__':
	myFIFO = myTestFIFOWithPoint()
	myFIFO.testFIFOWithPoint()