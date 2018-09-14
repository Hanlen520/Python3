# # eg1
# print("please input a number:")
# a = input()
# a = int(a)
# print("result is :",a+a)

# 加减乘除


# eg2:
print("please input the first number")
num1 = int(input())
print("please input the second number")
num2 = int(input())

# 求和
def sum():
    sum = num1 + num2
    print("sum is :%d" %sum)
sum()

# print("sum is:",num1+num2)

# 减法
def imsub():
    imsub = num1 - num2
    print("差为:",imsub)
imsub()

# 乘法
def product():
    product = num1*num2
    print("乘积为:",product)
product()

# 除法
def quotient():
    quotient = num1/num2
    print("两数相除为:",quotient)
quotient()