# 画五角星
import turtle
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)


# 画正弦图像
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.show()