# @Version  : 1.0
# @Author   : mmh
# @File     : 03_对象的传递机制.py
# @Time     : 2024/11/7 15:19
class Person:
    age = None
    name = None


# p1 = Person()
# p1.age = 10
# p1.name = "小明"
# p2 = p1
# print(p2.age)
# print(f"p1.name的地址：{id(p1.name)} p2.name地址：{id(p2.name)}")

a = Person()
a.age = 10
a.name = "jack"
b = a
print(b.name)
b.age = 200
b = None
print(a.age)
print(b.age)
