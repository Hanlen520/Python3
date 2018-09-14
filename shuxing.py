# 类Human
class Human:
    # 类共有属性
    name = 'wahaho'
    age = '20'
    gender = 'female'
    # 类私有属性
    __money = 6666

    def say(self):
        print('my name is :%s , moeny is :%d' %(self.name,self.__money))
        self.__lie()

    #私有方法
    def  __lie(self):
        print('i have 1111')

zhangsan = Human()
zhangsan.name = 'zhangsan'
# print (zhangsan.name)
# print (Human.name)

zhangsan.say()
# zhangsan.__lie()   私有方法不能在此调用