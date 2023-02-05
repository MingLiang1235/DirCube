#coding:cp936
import wx
import win32con,win32api,os
import codecs
import re
class MyFrame(wx.Frame):
	"""MyFrame clas treat with the config files"""
	def __init__(self):
		win32all_mode = ((win32con.FILE_ATTRIBUTE_DIRECTORY,  'd'),
                         (win32con.FILE_ATTRIBUTE_ARCHIVE,    'A'),
                         (win32con.FILE_ATTRIBUTE_COMPRESSED, 'C'),
						 (win32con.FILE_ATTRIBUTE_HIDDEN,     'H'),
						 (win32con.FILE_ATTRIBUTE_NORMAL,     'N'),
						 (win32con.FILE_ATTRIBUTE_READONLY,   'R'),
						 (win32con.FILE_ATTRIBUTE_SYSTEM,     'S'))
		UNAVAILABLE   = "Unavailable"
		global updateFile
		global medviewFile
		updateFile=''
		medviewFile=''
		def prepareTwoConfigFile():
			global updateFile
			global medviewFile
			updateFile=openFile(updateFPath)
			updateFile=subFile(updateFile)
			medviewFile=openFile(medviewFPath)
			medviewFile=subFile(medviewFile)
		def SaveConfig(text,filePath):
			#print 'text=' + text
			#print 'path=' + filePath
			if not (text==""):
				fopen = codecs.open(filePath,'w',encoding='utf8')
				fopen.write(text)
			else:
				pass
				#print "cant save because text is empty"
		def OpenTheFile(event):
			filePath = configFPath
			fopen = codecs.open(filePath,'r',encoding='utf8')
			contentsText.SetValue(fopen.read())
			contentsText.SetEditable(False)
		def SaveFile(event):
			contents = contentsText.GetValue()   #？？？？？？？？？？？？？？？？？？？？？？？？？
			if len(contents) > 0:
				filePath = configFPath
				fopen = codecs.open(filePath,'w',encoding='utf8')
				fopen.write(contentsText.GetValue())
				consoleText.AppendText(contents)
				consoleText.AppendText("Have saved.\n")
			else:
				consoleText.AppendText("the config is empty.\n")
			global updateFile
			global medviewFile
			#print 'updatefile=' + updateFile
			if (updateCheck.GetValue() == True and len(updateFile)!=0):
				print "want to save updateconfig"
				SaveConfig(updateFile,updateFPath)
			if (medviewCheck.GetValue() == True and len(medviewFile)!=0):
				print "want to save medviewconfig"
				SaveConfig(medviewFile,medviewFPath)
		def MatchText(event):
			contentsText.SetDefaultStyle(wx.TextAttr("red","blue"))
			consoleText.SetDefaultStyle(wx.TextAttr(wx.RED))
			consoleText.AppendText("Red text\n")
			#consoleText.SetValue(candidate+'Regex match?\n')
			text = contentsText.GetValue()
			reg = conditionText.GetValue()  # default use : r"getted value"
			print reg +'\n'
			m = re.search(reg, text)
			if m:
				consoleText.AppendText('Match onece!\n')
				#print  m.group(0)+"::"+m.group(1)+'\n'
				print  m.group(0)+"::"+'\n'
			else:
				consoleText.AppendText('not match\n')
				print "not match (search)"
		def SubTheText(event):
			consoleText.SetValue(candidate+'Regex match?\n')
			text = contentsText.GetValue()
			#reg = r' *<endpoint address="[a-zA-Z0-9<>:.]+//([a-zA-Z0-9_.:]+)'
			reg = conditionText.GetValue()  # default use : r"getted value"  r mean raw string (failure escape charater)
			p = re.compile(reg)
			#m = p.sub('hello', text)
			#print m			
			def func(m):
				return m.group(1)+replText.GetValue()
			repledText = p.sub(func,text)
			contentsText.SetValue(repledText)
			#print reg
			prepareTwoConfigFile()
		def verModify(event):
			versionFPath = workPath + '\MeDSysUpdate\MedSysUpdate.ini'
			fopen = codecs.open(versionFPath,'r',encoding='utf8')
			text=fopen.read()
			fopen.close()
			consoleText.AppendText(text+'<<------------------------>>\n')
			reg = '(AppVer=)([0-9]+.[0-9]+.[0-9]+.[0-9]+)'
			s = re.compile(reg)
			def func(m):
				return m.group(1)+updateVersionText.GetValue()
			repledText = s.sub(func,text,1)
			consoleText.AppendText(repledText)
			
			def getModes(fn):
				#print fn
				modlen = len(win32all_mode)
				#print modlen
				try:
					#print 'be in try'
					win32stat = win32api.GetFileAttributes(fn)
					#print 'getFileAttributes'
					mode = ""
					#print 'mode='+mode
				except:
					mode = UNAVAILABLE
  
				if not mode:
  
				# Test each attribute and set symbol in respective
				# position, if attribute is true.
					for i in range(modlen):
						mask, sym = win32all_mode[i]
						if win32stat & mask:
							mode += sym
						else:
							mode += '-'
				return mode
			mode = getModes(versionFPath)
			consoleText.AppendText(mode)
			for c in mode:
				if c == 'H':
					win32api.SetFileAttributes(versionFPath, win32con.FILE_ATTRIBUTE_NORMAL) 
			fsave = codecs.open(versionFPath,'w',encoding='utf8')
			fsave.write(repledText)
			win32api.SetFileAttributes(versionFPath, win32con.FILE_ATTRIBUTE_HIDDEN)
		def openFile(path):
			fopen = codecs.open(path,'r',encoding='utf8')
			text = fopen.read()
			return text
		def subFile(text):
			reg = conditionText.GetValue()
			p = re.compile(reg)
			def func(m):
				return m.group(1)+replText.GetValue()
			repledText = p.sub(func,text)
			return repledText
		wx.Frame.__init__(self,None,-1,u"TextTreater's 修改本  v.1_win_6",size=(900,535))
		panel = wx.Panel(self ,-1)
		#panel.Bind(wx.EVT_BUTTON, self.OnMove)
		#wx.StaticText(panel,-1,"Pos:",pos=(10,12))
		#self.posCtrl = wx.TextCtrl(panel,-1,"",pos=(40,10))
		loadButton = wx.Button(panel,label = 'load', pos=(225,5),size=(80,25))
		saveButton = wx.Button(panel,label = 'save', pos=(315,5),size=(80,25))
		matchButton = wx.Button(panel,label = 'search', pos=(315,5),size=(80,25))
		verModifyButton = wx.Button(panel,label = 'modify', pos=(355,5),size=(80,25))
		subButton = wx.Button(panel,label = 'sub', pos=(385,5),size=(80,25))
		
		locationText = wx.TextCtrl(panel, pos=(5,5),size=(200,25))
		mainConfigText = wx.TextCtrl(panel, pos=(5,5),size=(210,25))
		versionText = wx.TextCtrl(panel, pos=(5,5),size=(100,25))
		updateVersionText = wx.TextCtrl(panel, pos=(5,5),size=(100,25))
		workLocalLabel = wx.StaticText(panel, -1, u"当前工作位置:")
		mainConfigLabel = wx.StaticText(panel, -1, u"主配置文件:")
		versionLabel = wx.StaticText(panel, -1, u"版本号:")
		updateVersionLabel = wx.StaticText(panel, -1, u"版本升级号:")
		conditionText = wx.TextCtrl(panel, size=(300,25))
		replText = wx.TextCtrl(panel, size=(300,25))
		updateCheck = wx.CheckBox(panel,-1,"UpdateDir",(35,40),(80,25))
		medviewCheck = wx.CheckBox(panel,-1,"MedviewDir",(35,60),(80,25))
		contentsText = wx.TextCtrl(panel,pos=(5,35),size=(395,260),style=wx.TE_MULTILINE|wx.HSCROLL)
		consoleText = wx.TextCtrl(panel,pos =(405,35),size=(100,260),style=wx.TE_MULTILINE|wx.HSCROLL)
		
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(workLocalLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(locationText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox.Add(mainConfigLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(mainConfigText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox.Add(updateCheck,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(medviewCheck,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(versionLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(versionText,proportion=0,flag=wx.LEFT,border=17)
		hbox2.Add(updateVersionLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(updateVersionText,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(verModifyButton,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(conditionText,proportion=1,flag=wx.LEFT,border=5)
		hbox2.Add(matchButton,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(replText,proportion=1,flag=wx.LEFT,border=5)
		hbox2.Add(subButton,proportion=0,flag=wx.LEFT,border=5)
		
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(contentsText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox3.Add(consoleText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)		
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
		vbox.Add(hbox2,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		vbox.Add(hbox3,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		#vbox.Add(contentsText,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		
		panel.SetSizer(vbox)
		
		loadButton.Bind(wx.EVT_BUTTON,OpenTheFile)
		saveButton.Bind(wx.EVT_BUTTON,SaveFile)
		matchButton.Bind(wx.EVT_BUTTON,MatchText)
		verModifyButton.Bind(wx.EVT_BUTTON,verModify)
		subButton.Bind(wx.EVT_BUTTON,SubTheText)
		#contentsText.SetDefaultStyle(wxTextAttr(wxRED,wxWHITE))  #why does this not work
		candidate =  r"(\w+)\s"
		candidate += "\n"
		candidate += r" *[a-zA-z_0-9<>]+"
		candidate += "\n"
		candidate += r' *<endpoint address="(net.tcp)'
		candidate += "\n"
		candidate += r' *<endpoint address="[a-zA-Z0-9<>:.]+//([a-zA-Z0-9_.:]+)'
		candidate += "\n=====================\n"
		consoleText.SetValue(candidate)
		
		repl = "172.17.0.87:8080"
		replText.SetValue(repl)
		workPath = 'd:\Program Files'
		try:
			GetFileVersionInfoPath = workPath + '\pride\PRIDE.exe'
			info = win32api.GetFileVersionInfo(GetFileVersionInfoPath, "\\")
			ms = info['FileVersionMS']
			ls = info['FileVersionLS']
			__version__ = "%d.%d.%d.%d" % (win32api.HIWORD(ms), win32api.LOWORD (ms),win32api.HIWORD (ls), win32api.LOWORD (ls))
		except:
			__version__ = '5.1.1.000' # some appropriate default here.

		try:
			versionFPath = workPath + '\MeDSysUpdate\MedSysUpdate.ini'
			fopen = codecs.open(versionFPath,'r',encoding='utf-8')
			reg = 'AppVer=([0-9]+.[0-9]+.[0-9]+.[0-9]+)'
			s = re.search(reg,fopen.read())
			updateVersionText.SetValue(s.group(1))
		except:
			updateVersionText.SetValue('not found')
			
		configFPath = workPath + '\pride\PRIDE.exe.config'
		updateFPath = workPath + '\MeDSysUpdate\MeDSysUpdate.exe.config'
		medviewFPath = workPath + '\MeDViewer\MeDViewer.exe.config'
		locationText.SetValue(workPath)
		mainConfigText.SetValue(configFPath)
		versionText.SetValue(__version__)
		versionText.SetEditable(False)
		conditionText.SetValue('( *<endpoint address="[a-zA-Z0-9<>:.]+//)([a-zA-Z0-9_.:]+)')	#[a-zA-z_0-9]*
		"""debuging"""
		#print "Debug: file_version:" + __version__

	def to_unicode_or_bust(obj,encoding='utf-8'):
		if isinstance(obj,basestring):
			if not isinstance(obj,unicode):
				obj = unicode(obj,encoding)
		return obj
		
	#def OnMove(self,event):
     #   pos = event.GetPosition()
      #  self.posCtrl.SetValue("%s,%s" % (pos.x,pos.y))
	  
class MyApp(wx.App):
	"""MyApp class is an application class"""
	def OnInit(self):
		self.frame = MyFrame()
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
def main():
	app = MyApp()
	try:
		app.MainLoop()
	except:
		raw_input('Press any key to terminate the app')
	
if __name__=='__main__':
	main()
		
		
		