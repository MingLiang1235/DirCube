#coding:utf-8

import StackWithPoint

class myTestFIFOWithPoint(object):
	def testFIFOWithPoint(self):
		print "Now init fifo:"
		ls = [1,2,3,4]
		self.fifo = StackWithPoint.FIFOWithPoint(ls);
		print "Fifo fill with [1,1,2,3]."
		print "After init fifo:"
		print self.fifo
		print "The point is:" + str(self.fifo.getPoint())
		print "After pop:" + str(self.fifo.popit())
		print self.fifo
		print "The point is:" + str(self.fifo.getPoint())
		print "=========="
		print "<left right test>"
		print "Now push '4':"
		self.fifo.push(4)
		print self.fifo
		print "The Point is:" + str(self.fifo.getPoint())
		print "Now push [1,2,3,4,5]:"
		self.fifo.push([1,2,3,4,5])
		print self.fifo
		print "The Point is:" + str(self.fifo.getPoint())
		print "The Current is: " + str(self.fifo.getCurr())
		print "Now getRight:"
		print self.fifo.getRight()
		print "The Point is:" + str(self.fifo.getPoint())
		print "Now getLeft:"
		print self.fifo.getLeft()
		print "The Point is:" + str(self.fifo.getPoint())
		print "The current is: " + str(self.fifo.getCurr())
		print "Now getLeft twice:"
		print self.fifo.getLeft()
		print self.fifo.getLeft()
		print "The Point is:" + str(self.fifo.getPoint())
		print "=========="
		print "<point test>"
		print "The fifo before push :" + str(self.fifo)
		print "The point before push:" + str(self.fifo.getPoint())
		self.fifo.push(6)
		print "The fifo after push(6) :" + str(self.fifo)
		print "The point after push:" + str(self.fifo.getPoint())
		self.fifo.push(7)
		print "The fifo after push(7) :" + str(self.fifo)
		print "The point after push:" + str(self.fifo.getPoint())
		self.fifo.push(8)
		print "The fifo after push(8) :" + str(self.fifo)
		print "The point after push:" + str(self.fifo.getPoint())
		self.fifo.push(9)
		print "The fifo after push(9) :" + str(self.fifo)
		print "The point after push:" + str(self.fifo.getPoint())
		self.fifo.push(10)
		print "After push 10,the fifo is:" + str(self.fifo)
		print "The point is:" + str(self.fifo.getPoint())
		print "The curr is:" + str(self.fifo.getCurr())
		self.fifo.push(11)
		print "After push 11,the fifo is:" + str(self.fifo)
		print "The point is:" + str(self.fifo.getPoint())
		print "The curr is:" + str(self.fifo.getCurr())

		self.fifo.getLeft()
		self.fifo.getLeft()
		for i in range(5):
			self.fifo.push(i)
		print "After left and push,the fifo is:" + str(self.fifo)
		print "The point is:" + str(self.fifo.getPoint())
		print "The curr is:" + str(self.fifo.getCurr())

		print "\n Now clear fifo:"
		self.fifo.clearAll()
		print "Fifo is :" + str(self.fifo)
		print "Fifo 's len is :" + str(len(self.fifo))
		print "Fifo 's curr is" + str(self.fifo.getCurr())

		print "Append [] and some to fifo:"
		self.fifo.push([])
		self.fifo.push(1)
		self.fifo.push(2)
		self.fifo.push(3)
		print "New appended fifo is:"
		print self.fifo
		self.fifo.popit()
		self.fifo.popit()
		print "New deleted fifo is:"
		print self.fifo
		print "the point is:" + str(self.fifo.getPoint())

		print "=========="
		print "<Edge test>"
		self.fifo.clearAll()
		print "After clear, the point is:" + str(self.fifo.getPoint())
		for i in range(12):
			self.fifo.push(i)
			print "After push one,the point is:" + str(self.fifo.getPoint())
		print "Push 12 value:" + str(self.fifo)
		print "The point is:" + str(self.fifo.getPoint())
		print "Get right:" + str(self.fifo.getRight())
		print "The point is:" + str(self.fifo.getPoint())
		print "Get left:" + str(self.fifo.getLeft())
		print "the point is:" + str(self.fifo.getPoint())
		print "Get left:" + str(self.fifo.getLeft())
		print "the point is:" + str(self.fifo.getPoint())
		print "Get curr is:" + str(self.fifo.getCurr())
		print "the point is:" + str(self.fifo.getPoint())

		print "=========="
		print "<Other test>"
		print "Now clear fifo:"
		self.fifo.clearAll()
		self.fifo.push([])
		if self.fifo[0] == []:
			print "fifo0 is [] ok."
		else:
			print "fifo0 is [] not ok"
		print "And the time point is:" + str(self.fifo.getPoint())
		if self.fifo.getCurr() == []:
			print "fifo.curr is [] ok."
		else:
			print "fifo.curr is [] not ok."
		print "The fifo is:"
		print self.fifo
		print "push [1]:" 
		self.fifo.push([1])
		print "The point is :" + str(self.fifo.getPoint())
		print "The current is :" + str(self.fifo.getCurr())
		print "The left is :" +str(self.fifo.getLeft())
		print "The left is :" + str(self.fifo.getLeft())
		print "The Right is :" +str(self.fifo.getRight())
		print "The Right is :" + str(self.fifo.getRight())
if __name__ == '__main__':
	myFIFO = myTestFIFOWithPoint()
	myFIFO.testFIFOWithPoint()