# @Version  : 1.0
# @Author   : mmh
# @File     : 05_inheritance_detail.py
# @Time     : 2024/11/9 13:46
# 1.子类继承了所有的属性和方法，非私有的属性和方法可以在子类直接访问
# 但是私有属性和方法不能在子类直接访问
# 要通过父类提供公共的方法去访问

# class Base:
#     # 公共属性
#     n1 = 100
#     # 私有属性
#     __n2 = 200
#
#     def __init__(self):
#         print("Base 构造方法")
#
#     def hi(self):
#         print("hi() 公共方法")
#
#     def __hello(self):
#         print("__Hello__() 私有方法")
#
#     # 提供公共方法，返回私有的属性和方法
#     def test(self):
#         print("属性：",self.n1, self.__n2)
#
# class Sub(Base):
#     def __init__(self):
#         print("Sub 构造方法.....")
#
#     def say_ok(self):
#         # 我们发现父类的非私有属性和方法可以访问
#         print("say_ok()", self.n1)
#         self.hi()
#         # 我们发现父类的私有属性和方法不可以访问
#         # print(self.__n2)
#         # self.__hello()
#
# # 创建子类对象
# sub = Sub()
# sub.say_ok()
#
# # 子类只能根据父类提供的公共方法去访问私有成员
# sub.test()

class A:
    n1 = 100

    def sing(self):
        print("A sing()...", self.n1)

    def dance(self):
            print("A sing()...", self.n1)


class B:
    n2 = 200

    def dance(self):
        print("A sing()...", self.n2)


# C类继承了A，和B 类（多重继承）
# 在多重继承中，如果有同名的成员，遵守从左到右的继承优先级（左边的父类优先级高，写在右边的父类优先级低）
class C(A, B):
    # Python pass 是空语句，是为了保持程序结构的完整性
    # pass 不做任何事情，一般用做占用语句
    pass


c = C()
print("-------------------------------------")
# 继承的属性信息
print(f"属性信息 {c.n1} {c.n2}")
# 调用继承的方法
c.dance()
c.sing()