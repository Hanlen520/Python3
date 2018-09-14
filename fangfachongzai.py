# 方法重载
# 父类
class Father:
    money = 11111
    __money = 111
    def drive(self):
        print('have car')

class Mother:
    mm = 22222

class Son(Father,Mother):
    # 方法重载
    def drive(self):
        print('have tank')

        Father.drive(self)

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