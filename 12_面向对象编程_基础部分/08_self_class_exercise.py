# @Version  : 1.0
# @Author   : mmh
# @File     : 08_self_class_exercise.py
# @Time     : 2024/11/8 15:17
class Person:
    name = None
    age = None
    def compare_to(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

p1 = Person()
p1.name="小明"
p1.age=18
other = Person()
other.name="小明"
other.age=18
print(f"和另一个人是否相等：{p1.compare_to(other)}")