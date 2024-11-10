# @Version  : 1.0
# @Author   : mmh
# @File     : 31_homework01.py
# @Time     : 2024/11/10 16:13
class Person:
    name = None
    age = None
    job = None

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job={self.job})"


def sort(list: list):
    for i in range(len(list)-1):
        for j in range(len(list) - i - 1):
            if list[j].age < list[j + 1].age:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [Person("ming", 26, 'python工程师'),
        Person("mimi", 34, 'java工程师'),
        Person("tom", 27, "前端工程师")]

# sort(list)
# 2.方法2:使用使用列表的.sort
list.sort(key=lambda person: person.age,reverse=True)
print(list)



