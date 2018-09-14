# 聊天窗口
import wx
import time
class MyFrame (wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,
                         parent=None,
                         title="聊天窗口",
                         pos = (400,200),
                         size = (600,400))
        panel = wx.Panel(self,-1)
        labelAll = wx.StaticText(panel,-1,"好友",pos=(0,0))
        self.textAll = wx.TextCtrl(panel,
                                   -1,
                                   pos=(2,20),
                                   size=(600,200),
                                   style=wx.TE_READONLY | wx.TE_MULTILINE)
        labelIn = wx.StaticText(panel, -1, "我的",pos=(0,220))
        self.textIn = wx.TextCtrl(panel,
                                   -1,
                                   pos=(2, 240),
                                   size=(600, 100),
                                   style=wx.TE_MULTILINE)
        self.btnSent = wx.Button(panel,-1,"发送",size=(50,25),pos=(300,345))
        self.btnCancel = wx.Button(panel, -1, "取消", size=(50, 25), pos=(370, 345))
        # 绑定按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonCancel,self.btnCancel)

    def OnButtonSent(self,event):
        userinput = self.textIn.GetValue()
        self.textIn.Clear()
        now = time.ctime()
        inmsg = (now + "\n" + userinput + "\n")
        # self.textAll.SetValue(userinput)
        self.textAll.AppendText(inmsg)


    def OnButtonCancel(self,event):
        pass


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()

