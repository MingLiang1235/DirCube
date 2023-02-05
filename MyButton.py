#-*- encoding:UTF-8 -*-
import wx

class MyButton(wx.Button):
	def __init__(self,panel,i,label,position,size):
		wx.Button.__init__(self,panel,id=i,label=label,pos=position,size=size)
		self.Bind(wx.EVT_KEY_DOWN,self.keyDown)
	def keyDown(self,event):
		key = event.GetKeyCode()
		if (key == wx.WXK_F5) | (key==wx.WXK_RETURN):
			dlg = wx.MessageDialog(None,"push F5",'A Message',wx.OK | wx.ICON_INFORMATION)
			retCode = dlg.ShowModal()
		event.Skip()