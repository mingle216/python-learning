# @Version  : 1.0
# @Author   : mmh
# @File     : 11_construct_method.py
# @Time     : 2024/11/8 16:01
# class Person:
#     name = None
#     age = None
#
#     # 构造方法/构造器
#     # 构造方法是完成对象的初始人物
#
#
#     def __init__(self, name, age):
#         print(f"__init__ 执行了 {name} {age}")
#         print(f"self_id:{id(self)}")
#         # 1.把接收到的name和age赋给属性(name,age)
#         # 2.self就是你当前创建的对象
#         self.name = name
#         self.age = age
#
#
# # 创建对象
# p = Person("kobe",2)
# print(f"p id:{id(p)}")
# print(f"p 的信息:{p.age} {p.name}")
#
# p2=Person("tom",30)
# print(f"p2 id:{id(p2)}")
# print(f"p2 的信息:{p2.age} {p2.name}")

class Person:
    name = None
    age = None

    def __init__(self, name, age):
        print(f"__init__执行了。。。得到了{name}, {age}")
        self.name = name
        self.age = age


p1=Person("咪咪",2)
print(f"p1的name={p1.name}, age={p1.age}")
