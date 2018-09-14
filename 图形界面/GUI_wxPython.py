# '''对象化开发,'''
# import  wx
# #应用程序对象
# app = wx.App()
# # 框架窗口对象
# frame = wx.Frame(parent = None)
# # 显示框架窗口
# frame.Show()
# # 进入消息循环
# app.MainLoop()



# '''子类化开发'''
import wx
import turtle
class myApp(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = "hello",
                         size = (500, 300),
                         pos = (80,30))
        panel = wx.Panel(frame,-1)
        self.buttonst = wx.Button(panel,
                                  -1,
                                  "视图",
                                  size = (75,25),
                                  pos=(5,5))
        self.Bind(wx.EVT_BUTTON,self.OnButtonst,self.buttonst)
        self.buttonst.SetDefault()
        frame.Show()
        return True


    def OnButtonst(self,event):
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)

if __name__=="__main__":

    app = myApp
    app.MainLoop()


