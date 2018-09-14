# 闭包
def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a = hello_conf('morning!')
print(a.__name__)
print(id(a))
# a('milo')
# a('hehe')

b = hello_conf('afternoon!')
print(b.__name__)
print(id(b))
# b('hh')