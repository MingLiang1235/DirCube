#coding:utf-8

class FIFOWithPoint(list):
	def __init__(self,ls):
		# self.fifo = []
		self.sizeLimit = 10     
		self.point = -1
		# self.push(("",[]))
		for i in ls :
			self.push(i)



	def push(self,item):
		# if len(self)< self.sizeLimit:          #没有填满数列
		if self.point < self.sizeLimit-1 and len(self) ==self.sizeLimit:  #填满了数列，并且point在中间
			for i in range(self.sizeLimit-self.point-1):
				self.pop()
		if self.point < len(self)-1:                            #没有填满数列，并且point在中间
			for i in range(len(self)-self.point-1):
				self.pop()

		self.point +=1
		self.insert(self.point,item)     #在中间插入数值。

		# if (self.point >= -1) and (self.point < self.sizeLimit-1):
		# 	self.point += 1
		if len(self) > self.sizeLimit:                                  #数列已满，还添加新数据
			self.popit()
			# self.append(item)
			# if self.point < self.sizeLimit:
			# 	self.point += 1
			#self.point = self.sizeLimit-1
			if (self.point >= self.sizeLimit):   #如果指针也已满，
				self.point -= 1     #指针向左移一位

	def update(self,item):
		del self[self.point]               #先弹出一个
		self.insert(self.point,item)       #再在原地插入


	def popit(self):
		if self != []:
			temp = self[0]
			del self[0]
			if self.point > -1:
				self.point -= 1
			return temp
		else:
			return None

	def validPoint(self):
		if (self.point >= len(self)) or (self.point < -1):
			return False
		else:
			return True

	def getCurr(self):
		if self.validPoint():
			if self.point == -1:
				return None
			else:
				return self[self.point]
		else:
			return None

	def getRight(self):
		if self.validPoint():
			if self.point >= len(self)-1:
				self.point = len(self)-1
				return self[self.point]
			else:
				self.point += 1
				return self[self.point]
		else:
			return None

	def getLeft(self):                  
		if self.validPoint():
			if self.point == -1 or self.point == 0:
				self.point = 0
				return self[self.point]
			# elif self.point == 0:
			# 	self.point = -1
			# 	return None
			else:
				self.point -= 1
				return self[self.point]
		else:
			return None

	def getPoint(self):
		return self.point

	def getAll(self):
		return self

	def getSize(self):
		return len(self)

	def isEmpty(self):
		return self == []

	def clearAll(self):
		# self = list()
		for i in range(len(self)):
			self.popit()
		self.point = -1
		return len(self)
#--------------------------------------------------#
#	以上都ok       10-6-2018                       #
#--------------------------------------------------#