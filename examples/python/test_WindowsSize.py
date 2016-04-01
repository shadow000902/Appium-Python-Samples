# coding:gb2312
# wxApp.py
# author: aoogur
import os
import wx
from win32api import GetSystemMetrics

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title="wxApp.", size=(250, 250), pos=(0, 0))

        # 一种方法(wxPython)
        mm=wx.DisplaySize()
        print ("width=",mm[0])
        print ('height=',mm[1])
        #另一种方法
        print ("width =", GetSystemMetrics (0))
        print ("height =",GetSystemMetrics (1))
class App(wx.App):
    def OnInit(self):
        frame = Frame()
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = App(False)
    app.MainLoop()