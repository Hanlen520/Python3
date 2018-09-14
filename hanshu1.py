# 定义函数
num1 = int(input("请输入x值:"))

def f(num1):
    if num1 >= 1:
        return (num1 * 2)
    else:
        return abs(num1 * 2)
# abs 返回绝对值
result = f(num1)
print ("值为:%s" %result)