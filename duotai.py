# 多态
# 定义三角形的类
class Triangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height / 2
        return area

#定义正方形的类
class Square:
    def __init__(self,size):
        self.size = size
    def getArea(self):
        area = self.size * self.size
        return area

a = Triangle(2,5)
print(a.getArea())
b = Square(4)
print(b.getArea())



