# @Version  : 1.0
# @Author   : mmh
# @File     : 06_method_detail.py
# @Time     : 2024/11/8 13:11

def hi():
    print("hi,python")


class Person:
    name = None
    age = None
    def ok(self):
        print("ok,python")


p = Person()
p2 = Person()
"""
    1.动态的给p对象添加方法m1,注意只是针对p对象添加方法
    2.m1是你新添加的方法的名称，由程序员指定名字
    3.即m1方法和函数h1关联起来，当调用m1方法时，会执行hi函数
"""
p2.abc = hi
# 调用m1(即hi)
p2.abc()

