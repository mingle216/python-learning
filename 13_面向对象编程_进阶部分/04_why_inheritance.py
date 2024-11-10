# @Version  : 1.0
# @Author   : mmh
# @File     : 04_why_inheritance.py
# @Time     : 2024/11/9 13:33
# 使用继承的代码
# 编写父类Student
class Student:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name: {self.name}, age: {self.age}, score: {self.__score}")

    def set_score(self, score):
        self.__score = score

    def show_info(self):
        print(f"name: {self.name}, age: {self.age}, score: {self.__score}")


# 小学生-继承 Student
class Pupil(Student):

    def testing(self):
        return "...小学生在考小学数学..."


# 大学生-继承 Student
class Graduate(Student):
    def testing(self):
        return "...大学生在考高等数学..."


pupil = Pupil("xixi", 10)
pupil.set_score(90)
graduate = Graduate("ming", 18)
graduate.set_score(98)
print(graduate.testing())
graduate.show_info()
print(pupil.testing())
pupil.show_info()