# @Version  : 1.0
# @Author   : mmh
# @File     : 12_construct_method_detail.py
# @Time     : 2024/11/8 16:12

# 一个类只有一个 __init__方法，即使你写了多个，也只有最后一个生效
class Person:
    name = None
    age = None

    def __init__(self, name, age):
        print(f"__init__执行了。。。得到了{name}, {age}")
        self.name = name
        self.age = age

    # def __init__(self, name):
    #     print(f"__init__执行了。。。得到了{name}, {age}")
    #     self.name = name


# 报错
p1 = Person("kobe", 20)
# 后面的__init()__ 生效
# pi = Person("kobe")
print(f"p1的name={p1.name}, age={p1.age}")
