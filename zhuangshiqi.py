# 装饰器,deco是myfunc的装饰器
import time

def deco(fuu):
    def wrapper():
        startT = time.time()
        fuu()
        endT = time.time()
        msecs = (endT - startT) * 1000
        print('total time is: %s 毫秒' % msecs)
    return wrapper

@deco
def myfunc():
    print('myfunc start ……')
    time.sleep(2)
    print('myfunc end ……')

print('my name is',myfunc.__name__)
# myfunc = deco(myfunc)

print('#'*40)
print('my name is',myfunc.__name__)
myfunc()


