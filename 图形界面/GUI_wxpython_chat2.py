# 聊天窗口
import wx
import time
class MyFrame (wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,
                         parent=None,
                         title="聊天窗口",
                         size = (600,400))
        panel = wx.Panel(self,-1)
        labelAll = wx.StaticText(panel,-1,"好友")
        self.textAll = wx.TextCtrl(panel,
                                   -1,
                                   size=(600,200),
                                   style=wx.TE_READONLY | wx.TE_MULTILINE)
        labelIn = wx.StaticText(panel, -1, "我的")
        self.textIn = wx.TextCtrl(panel,
                                   -1,
                                   size=(600, 100),
                                   style=wx.TE_MULTILINE)
        self.btnSent = wx.Button(panel,-1,"发送",size=(50,25))
        self.btnCancel = wx.Button(panel, -1, "取消", size=(50, 25))
        # 绑定按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonCancel,self.btnCancel)

        # 布局管理器sizer
        btnSizer = wx.BoxSizer()
        btnSizer.Add(self.btnSent,proportion=0)
        btnSizer.Add(self.btnCancel,proportion=0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
        mainSizer.Add(labelIn, proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn, proportion=0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)


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

