#程序一:以下两行报错  IndexError: string index out of range
# s = 'hello'
# print(s[10])

# 程序二:
# try:
#     s = 'hello'
#     print(s[0])
# except IndexError:
#     # pass
#     print('error')
# else:
#     print('no error')


# 程序三:捕获异常
try:
    f = open('car.py','r')
    fr = f.read()
    print(fr)
finally:
    f.close()

# 程序四效果等同三
with open('car.py','r') as f:
    f.read()
