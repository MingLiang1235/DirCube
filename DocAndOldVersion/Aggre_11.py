#coding:cp936
"""version 11 :  获取窗口大小，随时调整窗口值并适当显示输出值大小。"""
import wx
import win32con,win32api,os,sys
from stat import *
from os.path import join, getsize
import codecs
import re
import os
import sys
import ctypes.wintypes
import win32gui
import DevideModule
import ChoiceRandomLs
#import DialogConsole
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
		global prideFile
		global ls
		ls = []
		prideFile=''
		updateFile=''
		medviewFile=''
		def getWindowSize():
			'''
			Function:获取当前程序窗口大小 
			Input：NONE 
			Output: NONE 
			author: authoriter 
			blog:http://blog.csdn.net/ 
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
			
			global width,height
			width = rect.right-rect.left
			height = rect.bottom-rect.top
			return (width,height)
			
		def getdirsize(dir):  
			'''get size 需要捕获异常并处理异常'''
			size = 0L  
			for root, dirs, files in os.walk(dir): 
				s = 0L
				listName = []
				for name in files:
					try:
						s += getsize(join(root,name))
					except WindowsError,e:
						consoleText.AppendText(" when manipulate the file "+ name +" trig WindowsError exception \n")
						pass
					
				size += s  
			return size 
		def OpenTheLocation(event):    #数据结构[{'fileName':name,'isDir':True},{'fileName':name2,'isDir':False},...]
			global ls
			global buttons
			sizes = []
			size = 0L
			dir_= locationText.GetValue()+'\\'
			fileNameList= os.listdir(dir_)
			
			for fname in fileNameList:
				pathName = dir_+fname
				pathStat = os.stat(pathName)
				#entity_fileName = {'fileName':pathName}
				if S_ISDIR(pathStat.st_mode):
					size=getdirsize(pathName)
					isDir = True
					#entity_fileName['isDir']=True
					#dict_fileNamesOneLevel.append(entity_fileName)
				else :
					size=os.path.getsize(pathName)
					isDir = False
					#entity_fileName['isDir']=False
					#dict_fileNamesOneLevel.append(entity_fileName)
				dictSize={'name':pathName,'size':size,'isDir':isDir,'pos':0,'w':0,'h':0}
				sizes.append(dictSize)
				
			#dialog.Add("NOW OPEN THE LOC:::::::::")
			#dialog.Add("the row of origin dir is :"+str(len(sizes))+'\n')
			
			#for i in range(len(sizes)):
				#dialog.Add(sizes[i]['name']+"->"+str(sizes[i]['size'])+'\n')
			#dialog.Add("---------------\n")
			
			ls = getMaxs(sizes)
			#sizes[:]=sizes[:maxButtons]
			#for i in range(len(ls)):
				#dialog.Add("getMaxed sizes( ls["+str(i)+"] ) is :  "+str(ls[i]['size']))

			ls=ChoiceRandomLs.ReUnitLs(ls)
			#for i in range(len(ls)):
				#dialog.Add("ReUnit ls["+str(i)+"] is : "+ str(ls[i]['size']))
			#dialog.Add("ReUnited ls is :  "+str(ls)+'\n')
			
			# self.d = DevideModule.DevideRec()
			theWindwoSize= getWindowSize()
			theWidth = theWindwoSize[0]
			theHeight = theWindwoSize[1]
			consoleText.AppendText("theWidth."+ str(theWidth) +"\ntheHeight."+str(theHeight)+"\n---------------\n")
			ls = DevideModule.devide(ls,theWidth/2,theHeight-posInit-titleHeight)    # posInit  Y轴起始位置  titleHeight 标题栏的高度
			
			#for i in range(len(ls)):
				#dialog.Add('L['+ str(i) +']: '+ str(ls[i])+"\n")
				#dialog.Add("---------------\n")
			#dialog.Add("in OpenLocation,before destroy Buttons is : "+str(buttons)+"\n")
			destroyButtons(buttons)
			consoleText.AppendText("\nThe devided ls(to generate buttton) 's len() is "+ str(len(ls)) +" \n---------------\n")
			j = generateButton(ls)
			consoleText.AppendText("Generated "+ str(j) +" buttons.\n---------------\n")
			#vbox0.Clear()
			#panel.Refresh()
			for i in range(j):    #len(ls) == maxButtons refer to getMaxs(ls).
				# if i < len(ls):
					consoleText.AppendText(ls[i]['name']+'->'+str(ls[i]['size'])+'\n')
					buttons[i].SetLabel(ls[i]['name']+' '+str(ls[i]['size']/1024.0/1024.0)+'M '+('isDir'if (ls[i]['isDir']) else 'isFile'))  #如果是File，则不可以goThrough下一步了，这个要处理。另外如果是File为何没有name和size值？
					tip = buttons[i].GetToolTip()
					tip.SetTip(buttons[i].GetLabel())
				# else:
					# buttons[i].SetLabel("None")
					# tip = buttons[i].GetToolTip()
					# tip.SetTip(buttons[i].GetLabel())
			consoleText.AppendText("===============\n")
		def getMaxs(ls):
			"""ls:list,in,return: ls,has 3 items,top 3 large size.
			To getMaxs the ls[i]['level'] which is larger
			"""
			#print "I'm in sort!"
			for i in range(len(ls)):
				max=ls[i]['size']
				for j in range(i+1,len(ls)):
					curr=ls[j]['size']  # from 1 :...
					if curr>max:
						max=curr
						temp=ls[i]
						ls[i]=ls[j]
						ls[j]=temp
			#print ls
			ls2=ls[:maxButtons]
			return ls2
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
				consoleText.AppendText(filePath+" saved.\n")
			else:
				consoleText.AppendText("Cant save because text "+filePath+" is empty.\n")
				#pass
				#print "cant save because text is empty"
		def OpenTheFile(event):
			global prideFile
			filePath = configFPath
			fopen = codecs.open(filePath,'r',encoding='utf8')
			prideFile = fopen.read()
			#contentsText.SetValue(prideFile)
			#contentsText.SetEditable(False)
		def SaveFile(event):
			global prideFile
			contents = prideFile
			if len(contents) > 0:
				filePath = configFPath
				fopen = codecs.open(filePath,'w',encoding='utf8')
				fopen.write(prideFile)
				#consoleText.AppendText(contents)
				consoleText.AppendText(filePath+" saved.\n")
			else:
				consoleText.AppendText("the config is empty.\n")
			global updateFile
			global medviewFile
			#print 'updatefile=' + updateFile
			if (updateCheck.GetValue() == True and len(updateFile)!=0):
				#print "want to save updateconfig"
				SaveConfig(updateFile,updateFPath)
			if (medviewCheck.GetValue() == True and len(medviewFile)!=0):
				#print "want to save medviewconfig"
				SaveConfig(medviewFile,medviewFPath)
		#def MatchText(event):
			#contentsText.SetDefaultStyle(wx.TextAttr("red","blue"))
			#consoleText.SetDefaultStyle(wx.TextAttr(wx.RED))
			#consoleText.AppendText("Red text\n")
			#consoleText.SetValue(candidate+'Regex match?\n')
			#text = contentsText.GetValue()
			#reg = conditionText.GetValue()  # default use : r"getted value"
			#print reg +'\n'
			#m = re.search(reg, text)
			#if m:
				#consoleText.AppendText('Match onece!\n')
				#print  m.group(0)+"::"+m.group(1)+'\n'
				#print  m.group(0)+"::"+'\n'
			#else:
				#consoleText.AppendText('not match\n')
				#print "not match (search)"
		def SubTheText(event):
			global prideFile
			text = prideFile
			#reg = r' *<endpoint address="[a-zA-Z0-9<>:.]+//([a-zA-Z0-9_.:]+)'
			reg = strconditionText  # default use : r"getted value"  r mean raw string (failure escape charater)
			p = re.compile(reg)
			#m = p.sub('hello', text)
			#print m			
			def func(m):
				return m.group(1)+replText.GetValue()
			repledText = p.sub(func,text)
			#consoleText.SetValue(candidate+'Regex match.\n')
			#consoleText.SetValue(candidate+'Content replaced..\n')
			consoleText.AppendText('Content has been replaced..\n')
			prideFile = repledText
			#contentsText.SetValue(repledText)
			#print reg
			prepareTwoConfigFile()
		def verModify(event):
			versionFPath = workPath + '\MeDSysUpdate\MedSysUpdate.ini'
			fopen = codecs.open(versionFPath,'r',encoding='utf8')
			text=fopen.read()
			fopen.close()
			
			reg = '(AppVer=)([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)'
			s = re.compile(reg)
			match = s.search(text)
			if match:
				consoleText.AppendText(match.group(0)+'\n'+'<<------------------------>>\n')
			def func(m):
				return m.group(1)+updateVersionText.GetValue()
			repledText = s.sub(func,text,1)
			match = s.search(repledText)
			if match:
				consoleText.AppendText(match.group(0)+'\n')
			
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
			consoleText.AppendText(mode+'\n')
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
			reg = strconditionText
			p = re.compile(reg)
			def func(m):
				return m.group(1)+replText.GetValue()
			repledText = p.sub(func,text)
			return repledText
		def goThrough(event):
			global ls
			if ls:
				for i in range(maxButtons):
					if i<len(ls):
						if event.GetEventObject()==buttons[i]:
							locationText.SetValue(ls[i]['name'])
			#触发一个open按钮的点击，用以触发打开工作位置的动作：
			#	。。。
		def generateButton(L):
			"""  L is the list with coordinate value 
			"""
			#pass
			#vbox0.Clear(True)
			global buttons
			i=0
			#vbox0= wx.BoxSizer(wx.VERTICAL)
			if buttons == None:
				buttons=[None]*maxButtons  # 重新初始化按钮列表
			consoleText.AppendText("in generate button,initaial Buttons is : "+str(buttons)+"\n")
			panel.ClearBackground() 
			panel.Refresh()
			self.Refresh()
			consoleText.AppendText("len(L): "+str(len(L))+"\n")
			
			for i in range(len(L)):
				position=(int(L[i]['pos'][0]),int(L[i]['pos'][1]))
				sizeofB = (int(L[i]['w']),int(L[i]['h']))
				buttons[i]=wx.Button(panel,id=i,label = str(i),pos = position,size=sizeofB)
				tip = wx.ToolTip('TEST')
				buttons[i].SetToolTip(tip)
				tip.SetTip(buttons[i].GetLabel())
				buttons[i].Bind(wx.EVT_BUTTON,goThrough)
				consoleText.AppendText("\nbutton("+str(i)+")):" + str(position) + "  "+str(sizeofB))
			consoleText.AppendText("\n---------------\n")
			# hbox3.Add(vbox0,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
			# hbox3.ShowItems(True)
			# vbox.ShowItems(True)
			
			return i+1   #生成了i+1个按钮
		def destroyButtons(buttons):
			for i in buttons:
				consoleText.AppendText("in DestroyButton,Button[i] is : "+str(i)+'\n')
				if i:
					i.Destroy()
					consoleText.AppendText(" --and it destroyed .\n")
					
		width = 900
		height = 535
		posInit = 65	#Y轴起始位置(工具栏的高度)
		titleHeight = 38	#标题栏的高度
		maxButtons = 12		#最大按钮数
		
		# devideRec = DevideRec.DevideRec()
		
		wx.Frame.__init__(self,None,-1,u"TextTreater's 查询器  v.0.7",size=(width,height))
		panel = wx.Panel(self ,-1)
		
		#self.dialog = DialogConsole.ConsoleDialog("===For Aggregation 1.0.9 === \n")
		#self.dialog.Show()
		
		#panel.Bind(wx.EVT_BUTTON, self.OnMove)
		#wx.StaticText(panel,-1,"Pos:",pos=(10,12))
		#self.posCtrl = wx.TextCtrl(panel,-1,"",pos=(40,10))
		loadButton = wx.Button(panel,label = '打开工作位置', pos=(225,5),size=(130,25))
		saveButton = wx.Button(panel,label = 'save', pos=(315,5),size=(80,25))
		#matchButton = wx.Button(panel,label = 'search', pos=(315,5),size=(80,25))
		verModifyButton = wx.Button(panel,label = 'modify', pos=(355,5),size=(80,25))
		subButton = wx.Button(panel,label = '替换', pos=(385,5),size=(80,25))
		
		locationText = wx.TextCtrl(panel, pos=(5,5),size=(200,25))
		#mainConfigText = wx.TextCtrl(panel, pos=(5,5),size=(210,25))
		versionText = wx.TextCtrl(panel, pos=(5,5),size=(120,25))
		updateVersionText = wx.TextCtrl(panel, pos=(5,5),size=(120,25))
		workLocalLabel = wx.StaticText(panel, -1, u":*当前位置*")
		#mainConfigLabel = wx.StaticText(panel, -1, u"主配置文件:")
		versionLabel = wx.StaticText(panel, -1, u"文件版本号:")
		updateVersionLabel = wx.StaticText(panel, -1, u"版本升级号:")
		#conditionText = wx.TextCtrl(panel, size=(300,25))
		replText = wx.TextCtrl(panel, size=(300,25))
		updateCheck = wx.CheckBox(panel,-1,"UpdateDir",(35,40),(80,25))
		medviewCheck = wx.CheckBox(panel,-1,"MedviewDir",(35,60),(80,25))
		#contentsText = wx.TextCtrl(panel,pos=(5,35),size=(395,260),style=wx.TE_MULTILINE|wx.HSCROLL)
		consoleText = wx.TextCtrl(panel,pos =(405,35),size=(100,260),style=wx.TE_MULTILINE)
		global buttons
		buttons = [None]*maxButtons   #一维数组初始法，二维初始法：A = [[None] * 2 for x in range(3)]  （这个是2×3的数组）
		# for i in range(maxButtons):
			# buttons[i]=wx.Button(panel,id=i,label = str(i),pos = (100,100*i),size=(180,55))
			# tip = wx.ToolTip('TEST')
			# buttons[i].SetToolTip(tip)
			# tip.SetTip(buttons[i].GetLabel())
		#firstButton = wx.Button(panel,label = 'first',pos=(100,100),size=(180,55))
		#secondButton = wx.Button(panel,label = 'second',pos=(100,200),size=(180,55))
		#thirdButton = wx.Button(panel,label = 'third',pos=(100,300),size=(180,55))
		
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(locationText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox.Add(workLocalLabel,proportion=0,flag=wx.LEFT,border=5)
		#hbox.Add(mainConfigLabel,proportion=0,flag=wx.LEFT,border=5)
		#hbox.Add(mainConfigText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox.Add(updateCheck,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(medviewCheck,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
		hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(versionLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(versionText,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(updateVersionLabel,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(updateVersionText,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(verModifyButton,proportion=0,flag=wx.LEFT,border=5)
		#hbox2.Add(conditionText,proportion=1,flag=wx.LEFT,border=5)
		#hbox2.Add(matchButton,proportion=0,flag=wx.LEFT,border=5)
		hbox2.Add(replText,proportion=1,flag=wx.LEFT,border=5)
		hbox2.Add(subButton,proportion=0,flag=wx.LEFT,border=5)
		
		vbox0 = wx.BoxSizer(wx.VERTICAL)
		#for i in buttons:
		#	vbox0.Add(i,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		# vbox0.Add(firstButton,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		# vbox0.Add(secondButton,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		# vbox0.Add(thirdButton,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(vbox0,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)
		hbox3.Add(consoleText,proportion=1,flag=wx.EXPAND|wx.LEFT,border=5)	
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
		vbox.Add(hbox2,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		vbox.Add(hbox3,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		#vbox.Add(contentsText,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
		
		panel.SetSizer(vbox)
		
		loadButton.Bind(wx.EVT_BUTTON,OpenTheLocation)
		saveButton.Bind(wx.EVT_BUTTON,SaveFile)
		#matchButton.Bind(wx.EVT_BUTTON,MatchText)
		verModifyButton.Bind(wx.EVT_BUTTON,verModify)
		subButton.Bind(wx.EVT_BUTTON,SubTheText)
		# for i in buttons:
			# i.Bind(wx.EVT_BUTTON,goThrough)
		# firstButton.Bind(wx.EVT_BUTTON,goThrough)
		# secondButton.Bind(wx.EVT_BUTTON,goThrough)
		# thirdButton.Bind(wx.EVT_BUTTON,goThrough)
		
		#contentsText.SetDefaultStyle(wxTextAttr(wxRED,wxWHITE))  #why does this not work
		#candidate =  r"(\w+)\s"
		#candidate += "\n"
		#candidate += r" *[a-zA-z_0-9<>]+"
		#candidate += "\n"
		#candidate += r' *<endpoint address="(net.tcp)'
		#candidate += "\n"
		#candidate += r' *<endpoint address="[a-zA-Z0-9<>:.]+//([a-zA-Z0-9_.:]+)'
		#candidate += "\n=====================\n"
		candidate = 'Console\n'
		candidate += 'D:\\oracle\\product\\10.2.0\\client_1\n'
		candidate += 'D:\\Life\n'
		candidate += '=======================\n'
		consoleText.SetValue(candidate)
		
		repl = "172.17.0.87:8080"
		replText.SetValue(repl)
		workPath = r'D:\oracle\product\10.2.0\client_1'
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
		#mainConfigText.SetValue(configFPath)
		versionText.SetValue(__version__)
		versionText.SetEditable(False)
		strconditionText='( *<endpoint address="[a-zA-Z0-9<>:.]+//)([a-zA-Z0-9_.:]+)'	#[a-zA-z_0-9]*
		"""debuging"""
		#print "Debug: file_version:" + __version__

	def to_unicode_or_bust(obj,encoding='utf-8'):
		if isinstance(obj,basestring):
			if not isinstance(obj,unicode):
				obj = unicode(obj,encoding)
		return obj
		
	#def OnDestroy(self):
		#self.dialog.Destroy()
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
	def OnDestroy(self):
		self.frame.Destroy()
		# self.frame.dialog.Destroy()
		# return True
def main():
	app = MyApp()
	try:
		app.MainLoop()
		
	except:
		raw_input('Press any key to terminate the app')
	
if __name__=='__main__':
	main()
		
		
		