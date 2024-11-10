# @Version  : 1.0
# @Author   : mmh
# @File     : 19_eq_magic_method.py
# @Time     : 2024/11/10 13:15
# @Version  : 1.0
# @Author   : mmh
# @File     : 19_eq_magic_method.py
# @Time     : 2024/11/10 11:47
class Person:
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    # 判断两个Person对象的内容是否相等
    # 如果两个Person对象的各个属性值都一样，则返回true，反之false
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and \
                self.age == other.age and \
                self.gender == other.gender
        else:
            return False
    # 小于
    def __lt__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age < other.age
        return "类型不一致，不能比较"

    # 小于等于
    def __le__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age <= other.age
        return "类型不一致，不能比较"
    # 不等于
    def __ne__(self, other):
        return not self.__eq__(other)

    # 大于
    def __gt__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age > other.age
        return "类型不一致，不能比较"

    # 大于等于
    def __ge__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return self.age >= other.age
        return "类型不一致，不能比较"



# 没有重写前 __eq__ 前，== 比较的是内存地址
p1 = Person("smith", 21, "男")
p2 = Person("smith", 20, "男")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 <= p2: {p1 <= p2}")
print(f"p1 != p2: {p1 != p2}")
print(f"p1 > p2: {p1 > p2}")
print(f"p1 >= p2: {p1 >= p2}")
