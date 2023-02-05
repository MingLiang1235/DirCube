#-*- encoding:UTF-8 -*-
import wx
from MyButton import *

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Test MyButton GUI")
		self.panel = wx.Panel(self)
		myButton = MyButton(self.panel, -1, "This is a MyButton",(30,10),(100,20))
		
		main = wx.BoxSizer(wx.HORIZONTAL)
		main.Add(myButton, 0, wx.RIGHT, 15)
		

		self.panel.SetSizer(main)

		self.Bind(wx.EVT_BUTTON, self.OnStartButton, myButton)
		
	def OnStartButton(self,event):
		print "pushStartButton"
		
		
app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()