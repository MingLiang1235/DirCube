#-*- encoding:UTF-8 -*-
#------------------------------------------------
# DialogConfig.py,config dialog of Aggre.py
# Writer: Jishan
# Date: 2019-1-9
# Version: 0.1
#------------------------------------------------
import wx
#------------------------------------------------
# Create and set a help provider.Normally you
# would do this in the app's OnInit as it 
# must be done before any SetHelpText calls.
provider = wx.SimpleHelpProvider()
wx.HelpProvider.Set(provider)
#------------------------------------------------
class TestDialog(wx.Dialog):
	"""docstring for TestDialog"""
	def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,style=wx.DEFAULT_DIALOG_STYLE, useMetal=False,maxButtons=36,conti=1,icon=None):
		#super(TestDialog, self).__init__()
		#self.arg = arg
		pre = wx.PreDialog()
		slider1Min = 10
		slider1Max = 50
		pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
		pre.Create(parent, ID, title, pos, size, style)

		self.PostCreate(pre)
		self.SetMinSize(size)
		if icon:
			self.SetIcon(icon)

		if 'wxMac' in wx.PlatformInfo and useMetal:
			self.SetExtraStyle(wx.DIALOG_EX_METAL)

		sizer = wx.BoxSizer(wx.VERTICAL)

		labTop = wx.StaticText(self,-1,u"设置")
		sizer.Add(labTop,0,wx.ALIGN_CENTER|wx.ALL,5)

		hori0 = wx.BoxSizer(wx.HORIZONTAL)
		labDefault = wx.StaticText(self,-1,u"启动选项")
		hori0.Add(labDefault,proportion=0,flag=wx.LEFT,border=5)
		hori0.Add((25,25),1,0,5)     #加入一段空白
		self.radio1 = wx.RadioButton(self,-1,u"打开全新界面",style=wx.RB_GROUP)
		self.radio2 = wx.RadioButton(self,-1,u"从上次停下的地方继续")
		vert = wx.BoxSizer(wx.VERTICAL)
		vert.Add(self.radio1,0,wx.EXPAND|wx.TOP|wx.BOTTOM,2)
		vert.Add(self.radio2,0,wx.EXPAND|wx.TOP|wx.BOTTOM,2)
		hori0.Add(vert,proportion=0,flag=wx.LEFT,border=5)

		hori = wx.BoxSizer(wx.HORIZONTAL)
		labSlider = wx.StaticText(self,-1,u"选择方块个数")
		# labSlider.SetHelpText("方块从12个到跟随实际的数量（不限制）")
		self.slider1 = wx.Slider(self,-1,slider1Min,slider1Min,slider1Max,style=wx.SL_HORIZONTAL|wx.SL_LABELS)
		self.slider1.SetHelpText(u"需要在屏幕上显示的方块个数")
		self.slider1.SetTickFreq(slider1Max,slider1Min)

		hori.Add(labSlider,0,wx.ALIGN_CENTER|wx.ALL,5)
		hori.Add(self.slider1,proportion=0,flag=wx.LEFT,border=5)

		sizer.Add(hori0,0,wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)
		sizer.Add(hori,0,wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)

		hori2 = wx.BoxSizer(wx.HORIZONTAL)
		self.checkbox = wx.CheckBox(self,01,u"使用实际数量",wx.DefaultPosition,wx.DefaultSize,0)
		self.checkbox.Bind(wx.EVT_CHECKBOX,self.checkIt)
		hori2.Add((50,25),1,0,5)          #添加入一块空白
		hori2.Add(self.checkbox,proportion=0,flag=wx.LEFT|wx.RIGHT,border=5)

		horiBtn = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(self,wx.ID_OK)
		btn2 = wx.Button(self,wx.ID_CANCEL)
		#btn.SetDefault()
		horiBtn.Add((50,25),1,0,5)			#添加一个size入horiBtn，建立填充空白。
		horiBtn.Add(btn1,0,wx.ALIGN_RIGHT,5)
		horiBtn.Add(btn2,0,wx.ALIGN_RIGHT,5)

		sizer.Add(hori2,0,wx.EXPAND|wx.TOP|wx.BOTTOM,5)
		sizer.Add(horiBtn,0,wx.EXPAND|wx.TOP|wx.BOTTOM,5)

		self.SetSizer(sizer)
		sizer.Fit(self)

		if (maxButtons != -1):
			self.slider1.Enable()
			if (maxButtons >= slider1Min and maxButtons <= slider1Max):
				self.slider1.SetValue(maxButtons)
			else:
				self.slider1.SetValue(slider1Min)
		else:
			self.slider1.Disable()
			self.checkbox.SetValue(True)
		if (conti == 1):
			self.radio1.SetValue(True)
			self.radio2.SetValue(False)
		else:
			self.radio1.SetValue(False)
			self.radio2.SetValue(True)

	def GetSliderValue(self):
		if not self.checkbox.IsChecked():
			return self.slider1.GetValue()
		else:
			return -1
	def GetRadioValue(self):
		if self.radio1.GetValue():
			return 0   #表示使用全新界面
		else:
			return 1   #表示从上次打开的地方继续

	def checkIt(self,evt):
		if self.checkbox.IsChecked():
			self.slider1.Disable()
		else:
			self.slider1.Enable()