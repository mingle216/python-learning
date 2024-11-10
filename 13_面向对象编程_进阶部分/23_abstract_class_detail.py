# @Version  : 1.0
# @Author   : mmh
# @File     : 23_abstract_class_detail.py
# @Time     : 2024/11/10 15:20
from abc import ABC, abstractmethod


class AAA(ABC):
    name = "tim"

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    def hi(self):
        print("hi()~~")

    def ok(self):
        pass


class BBB(AAA):
    # 实现父类的f1抽象方法
    def f1(self):
        print("bbb-f1()。。。")
    # 如果没有完成实现AAA的抽象方法，只有实现f1，那BBB此时还是一个抽象类
    # 不能实例化对象，需要将f2也实现完，才能实例化对象
    def f2(self):
        print("bbb-f2()。。。")


obj2 = BBB()
obj2.f1()
obj2.f2()
obj2.hi()
obj2.ok()
print("~~~~")
