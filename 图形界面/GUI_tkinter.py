'''创建窗口'''
# import tkinter
# 生成主窗口(面板)
# root = tkinter.Tk()
# 进入消息循环
# root.mainloop()

'''添加组件'''
import tkinter
import turtle
root = tkinter.Tk()

'''添加菜单'''
# 生成菜单
menu = tkinter.Menu(root)
# 生成下拉菜单
submenu = tkinter.Menu(menu,tearoff = 0)
# 下拉菜单添加Open
submenu.add_command(label = 'Open')
# 下拉菜单添加Save
submenu.add_command(label = 'Save')
# 将下拉菜单添加到菜单
menu.add_cascade(label = 'File',menu = submenu)
root.config(menu = menu)

# 生成标签
label = tkinter.Label(root,text = 'hello')
# 将标签添加至主窗口
label.pack()
# 生成按钮
button1 = tkinter.Button(root,text = '视图')
# 将按钮添加至主窗口
button1.pack()

# 事件响应函数
def ST(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
# 绑定事件(绑定了鼠标左键)
button1.bind('<Button-1>',ST)
# label.bind('<Button-1>',ST)



root.mainloop()