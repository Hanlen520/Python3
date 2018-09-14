# 继承
# 父类
class Father:
    money = 11111
    __money = 111
    def drive(self):
        print('have car')

class Mother:
    mm = 22222

#子类 只能继承公有属性,私有属性__money不可继承
class Son(Father,Mother):
    pass
    def pay(self):
        print(self.mm)

tom = Father()
print(tom.money)
tom.drive()

print('……'*20)

kingson = Son()
print(Son.money)
kingson.drive()
kingson.pay()