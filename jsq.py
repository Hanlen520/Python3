# 计算器
x = int(input("first:"))
o = input("operator:")
y = int(input("second:"))

# 字典
operator = {'+':x+y,
            '-':x-y,
            '*':x*y,
            '/':x/y}

if o == "+":
    print(x+y)
elif o == "-":
    print(x+y)
elif o == "*":
    print(x*y)
elif o == "/":
    print(x/y)
else:
    pass


# 方法二:
# result = ()
# while 1:
#     x = int(input("first:"))
#     o = input("operator:")
#     y = int(input("second:"))
#
#     operator = {'+': x + y,
#                 '-': x - y,
#                 '*': x * y,
#                 '/': x / y}
#
#     if o in operator:
#         result = operator.get(o)
#         print(result)
#     else:
#         print('please input + , - , * , /')
#         break;


