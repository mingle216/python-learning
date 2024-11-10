# @Version  : 1.0
# @Author   : mmh
# @File     : 09_override.py
# @Time     : 2024/11/9 18:20
class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("自我介绍：", self.name, self.age)


class Student(Person):
    id = None
    score = None

    def __init__(self, name, age, score, id):
        super().__init__(name, age)
        self.score = score
        self.id = id

    def say(self):
        print("自我介绍：", self.id, self.name, self.score, self.age)


p = Person("tom", 18)
s = Student("jack", 25, 90, "001")
s.say()
