#coding:utf-8
import threading
import os
import wx
from stat import *
class GetAllSizeThread(threading.Thread):
	"""docstring for GetAllSizeTread
	多线程处理特定目录总大小问题"""
	def __init__(self, dir,window):
		threading.Thread.__init__(self)
		self.dir = dir
		self.window = window
		self.stopEvent = threading.Event()
		self.stopEvent.clear()
	def stop(self):
		self.stopEvent.set()
	def getDirSize(self,dir):
		size = 0L  
		for root, dirs, files in os.walk(dir): 
			s = 0L
			listName = []
			for name in files:
				try:
					s += os.path.getsize(os.path.join(root,name))
				except WindowsError,e:
					msg = " when manipulate the file "+ name +" trig WindowsError exception \n"
					wx.CallAfter(self.window.consoleText.AppendText,msg)
					pass			
			size += s  
		return size
	def run(self):  #运行一个进程
		sizes = []
		try:
			wx.CallAfter(self.window.consoleText.AppendText,"\n THe Thread run.\n")
			fileNameList= os.listdir(self.dir)
			for fname in fileNameList:
				pathName = self.dir+fname
				pathStat = os.stat(pathName)
				if S_ISDIR(pathStat.st_mode):
					size = self.getDirSize(pathName)
					isDir = True
				else:
					size=os.path.getsize(pathName)
					isDir = False
				dictSize={'name':pathName,'size':size,'isDir':isDir,'pos':0,'w':0,'h':0}
				sizes.append(dictSize)
			wx.CallAfter(self.window.consoleText.AppendText,"the thread work done.\n")
			wx.CallAfter(self.window.DoneWithGetAllSize,sizes)
		except:
		# 	wx.CallAfter(self.window.consoleText.AppendText,self.dir)
		 	wx.CallAfter(self.window.consoleText.AppendText,"\n The work object Is a File,or invalide, can't open it.\n")
		 	wx.CallAfter(self.window.SimpleStopThread)
		

