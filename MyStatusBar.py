#-*- encoding:UTF-8 -*-
import wx
from wx.lib.agw.hyperlink import *

class MyStatusBar(wx.StatusBar):
	def __init__(self,parent):
		wx.StatusBar.__init__(self,parent,-1)

		self.SetFieldsCount(2)
		self.SetStatusWidths([-5,-3])

		self.sizeChanged = False
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_IDLE, self.OnIdle)
		#self.SetStatusText("Unicodes gearmaster @ copyRight 2015-2019", 0)   #write st to field[0]
		#This will fill into field 1 (the second field)
		# self.st = wx.StaticText(self,-1,"Donate..")
		# self.font = wx.Font(-1,wx.SWISS,wx.NORMAL,wx.NORMAL,True)
		# self.st.SetFont(self.font)
		rect = self.GetFieldRect(1)
		self.pos = (rect.x+2,rect.y+2)
		self.size = (rect.width-4,rect.height-4)
		self.SetStatusText("@copyRight 2019", 1)   # write st to field[1]
		##在field[1]写入捐款超链接
		#self.st = HyperLinkCtrl(self,-1,"Donate...",self.pos,self.size,
		#	style=0,name="hyperLinkCtrl",URL="https://jishan.asuscomm.com:6001/index.html?obj=5")  #write user default content to field[1]
		#self.st.Bind(wx.EVT_LEFT_DOWN,self.OnMouseUp)
		#set the initial position of the checkbox
		#self.Reposition()

	def OnSize(self, evt):
		#self.Reposition()  #用hyperLinkCtrl时要用到它
		self.sizeChanged = True
		evt.Skip()

	def OnIdle(self,evt):
		#if self.sizeChanged:  #用hyperLinkCtrl时要使能这两句
		# 	self.Reposition()
		evt.Skip()
	#///////////////////////////////////////////////
	# 当使用hyperLinkCtrl时，使能本方法。
	# def Reposition(self):
	# 	rect = self.GetFieldRect(1)
	# 	self.st.SetPosition((rect.x+2,rect.y+2))
	# 	self.st.SetSize((rect.width-4,rect.height-4))
	# 	self.sizeChanged = False
	#///////////////////////////////////////////////
	# def OnMouseUp(self,evt):
	# 	dlg = wx.MessageDialog(None,"Click donate","A Message box",wx.OK | wx.ICON_INFORMATION)
	# 	rtCode = dlg.ShowModal()
	# 	wx.wxLaunchDefaultBrowser("http://samgear.synology.me", wxBROWSER_NEW_WINDOW)
	# 	#aHLC = wxHyperlinkCtrl.Creat(self,-1,"Donate...","http://samgear.synology.me")
	# 	evt.Skip()