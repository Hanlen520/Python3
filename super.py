# # 方法一:
# class A:
#     def __init__(self):
#         print("enter A")
#         print("leave A")
# class B(A):
#     def __init__(self):
#         print("enter B")
#         A.__init__(self)
#         print("leave B")
# class C(A):
#     def __init__(self):
#         print('enter C')
#         A.__init__(self)
#         print('leave C')
# class D(B,C):
#     def __init__(self):
#         print('enter D')
#         B.__init__(self)
#         C.__init__(self)
#         print('leave D')
# d = D()

# 若要更换类A的的名字为AA,则所以用到A的地方都需要更换为AA,用super可避免
class A:
    def __init__(self):
        print("enter A")
        print("leave A")
class B(A):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")
class C(A):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')
class D(B,C):
    def __init__(self):
        print('enter D')
        super(B, self).__init__()
        super(C, self).__init__()
        print('leave D')
d = D()
