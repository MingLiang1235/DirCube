#-*- encoding:UTF-8 -*-
import wx

class Progress(object):
	def __init__(self,window,size):
		#self.note = u"Searching"
		self.note = u"请稍候"
		self.window = window
		self.size = size
		self.w,self.h = size
		self.timer = wx.Timer(owner=None,id=-1)
		self.timer.Bind(wx.EVT_TIMER,self.updateProgress)
		window.panel.Bind(wx.EVT_SIZE,self.onMyResize)
		self.font = wx.Font(36, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
		self.pro = wx.StaticText(self.window.panel, -1, self.note+"|",(self.w/2-100, self.h/2),size=(50,50))
		self.pro.SetFont(self.font)
		self.pattern = ["|","/","-","\\"]
		self.i = 0
		self.timer.Start(milliseconds=1000,oneShot=False)
	def updateProgress(self,event):
		if self.pro:                 #如果没有显示进度条，改变窗口大小也不显示之。
			s = (self.w,self.h)
			#print "onUpdateProgress:"+str(self.w)+" "+str(self.h)
			self.showIt(s)
	def onMyResize(self,event):
		if self.pro:                 #如果没有显示进度条，改变窗口大小也不显示之。
			self.w,self.h = event.Size
			#print "onMyREsize:"+str(self.w)+" "+str(self.h)
			self.showIt(event.Size)
		event.Skip()
	def showIt(self,size):
		w,h = size
		if (self.i < 3 ):
			self.i += 1
		else:
			self.i = 0
		#self.pro.setLabel(self.pattern[self.i])
		if self.pro:
			self.pro.Destroy()
		#print "in showIt.\n"
		self.pro = wx.StaticText(self.window.panel,-1,self.note+self.pattern[self.i],(w/2-100,h/2),size=(100,100))
		self.pro.SetFont(self.font)
	def stopProgress(self):
		if self.timer:
			self.timer.Stop()
			self.timer.Destroy()
		if self.pro:
			self.pro.Destroy()