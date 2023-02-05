#-*- encoding:UTF-8 -*-
import wx
from Progress import *
import win32con,win32gui,os,win32api
import ctypes.wintypes

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Test Prograss GUI")
		self.panel = wx.Panel(self)
		btnStart = wx.Button(self.panel, -1, "Start a Progress")
		btnStop = wx.Button(self.panel, -1, "Stop a Progress")

		main = wx.BoxSizer(wx.HORIZONTAL)
		main.Add(btnStart, 0, wx.RIGHT, 15)
		main.Add(btnStop, 0, wx.RIGHT, 15)

		self.panel.SetSizer(main)

		self.Bind(wx.EVT_BUTTON, self.OnStartButton, btnStart)
		self.Bind(wx.EVT_BUTTON, self.OnStopButton, btnStop)
	def OnStartButton(self,event):
		print "pushStartButton"
		
		size = self.getFrmSize()
		dlg = wx.MessageDialog(None, str(size),'A Message Box',wx.OK | wx.ICON_INFORMATION)
		retCode = dlg.ShowModal()
		# try:
		# 	self.Pro = Progress(self,size)
		# except Exception,err:
		# 	print str(err)
		self.Pro = Progress(self,size)
	def OnStopButton(self,event):
		if self.Pro:
			self.Pro.stopProgress()
	def getFrmSize(self):
		'''
		Function:获取当前程序窗口大小 
		Input：NONE 
		Output: tuple(width,height)  tuple 窗口大小 
		author: SamJi 
		blog:http://blog.csdn.net/cava15 
		date:2014-03-12'''
		#窗口结构         
		class RECT(ctypes.Structure):  
			_fields_ = [('left', ctypes.c_long),  
					('top', ctypes.c_long),  
					('right', ctypes.c_long),  
					('bottom', ctypes.c_long)]  
			def __str__(self):  
				return str((self.left, self.top, self.right, self.bottom))
		rect = RECT()
		#获取当前窗口句柄  
		HWND = win32gui.GetForegroundWindow()
		
		#取当前窗口坐标  
		ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))

		#global width,height
		width = rect.right-rect.left
		height = rect.bottom-rect.top
		return (width,height)



app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()