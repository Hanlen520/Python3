# 运算符重载
class Mylist:
    __mylist = []
    def __init__(self,*args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)
# 列表遍历加x
    def __add__(self, x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + x
        return self.__mylist

    def __sub__(self, x):
        pass
    def __mul__(self, x):
        pass
    def __div__(self, x):

        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / x
        return self.__mylist


    def show(self):
        print(self.__mylist)

if __name__ == '__main__()':
    l = Mylist(2,4,6,8)
    l + 10
    l / 2

    l.show()