from  functools import reduce

# 方法一:
# def  f(x,y):
#     return x+y
# reduce(f,[1,2,3,4,5])
# print()

# 方法二:
# sum = lambda x,y:x+y
# sum  (2,3)


# 方法三匿名函数:
reduce(lambda x,y:x+y,[1,2,3,])