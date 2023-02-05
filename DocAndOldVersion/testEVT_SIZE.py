# -*- coding:utf-8 -*-  
''''' 
Created on 2013-1-6 
 
@author: jincheng 
'''  
  
import wx  
#import com.jincheng.AbstractModel as jca  
#import com.jincheng.common as jcc  
  
class myFrame(wx.Frame):  
    def __init__(self,parent,title,size):  
        wx.Frame.__init__(self,parent,-1,title,size = size)  
        self.SetBackgroundColour('white')  
          
        #布局 size  
        self.width = self.Size.width  
        self.height = self.Size.height  
        self.up = self.Size.height/3*2  
        self.down = self.Size.height/3  
        self.left = self.Size.width/4  
        self.right = self.Size.width/4*3  
          
        #上下结构  
        self.spltUD = wx.SplitterWindow(self,size = size)  
          
        self.winUp = wx.Window(self.spltUD,-1,(0,0),(self.width,self.up))  
        self.winUp.SetBackgroundColour('red')  
  
        self.winDown = wx.Window(self.spltUD,-1,(0,self.up),(self.width,self.down))  
        self.winDown.SetBackgroundColour('black')  
          
        self.spltUD.SplitHorizontally(self.winUp,self.winDown,-10)  
  
        #左右结构  
        self.spltLF = wx.SplitterWindow(self.winUp,size = (self.width,self.up))  
  
        self.winLeft = wx.Window(self.spltLF,-1,(0,0),(self.left,self.up))  
        self.winLeft.SetBackgroundColour('yellow')  
          
        self.winRight = wx.Window(self.spltLF,-1,(0,self.left),(self.right,self.up))  
        self.winRight.SetBackgroundColour('green')  
          
        self.spltLF.SplitVertically(self.winLeft,self.winRight,-10)  
          
        #事件绑定  
        self.Bind(wx.EVT_SIZE,self.OnSize)  
          
    def OnSize(self,event):  
        size = event.Size  
        self.spltUD.Size=event.Size  
        self.spltLF.Size=(size.width,size.height - self.winDown.Size.height)  
  
if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = myFrame(None,'title',(800,600))  
    frame.Show(True)  
    app.MainLoop()