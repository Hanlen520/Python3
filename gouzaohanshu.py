class Human:
    name = 'yuu'
    age = '25'
    gender = 'female'
    __money = 6666

    # 构造函数__init__(特殊方法,内置方法),初始化对象
    def __init__(self,name,age):
        print('_'*50)
        # name是实例的属性
        self.name = name
        self.age = age
        print('_' * 50)



'''
    def __str__(self):
        msg = 'hi!!!'
        return msg
'''

'''
    def say(self):
        print('name is: %s,age is %d' %(self.name,self.__money))
        self.__lie()

    def __lie(self):
        print('i have 1111')
'''

zhangsan = Human('zhangsan',33)
print(zhangsan.name,zhangsan.age)



# print(zhangsan)

# # 打印类的属性
# print (Human.name)