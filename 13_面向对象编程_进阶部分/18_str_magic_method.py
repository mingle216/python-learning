# @Version  : 1.0
# @Author   : mmh
# @File     : 18_str_magic_method.py
# @Time     : 2024/11/10 11:29
class Monster:
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 输出Monster[name,job,sal]对象的属性信息
    # 根据需要重写__str__
    # 1.默认情况调用的是父类object的__str__
    # 2.父类object的__str__ 返回的就是类型+地址
    # 3.可以根据需要重写__str__
    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"

m = Monster("青牛怪",500,"男")
print(m)
