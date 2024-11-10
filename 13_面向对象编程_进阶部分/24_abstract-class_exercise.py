# @Version  : 1.0
# @Author   : mmh
# @File     : 24_abstract-class_exercise.py
# @Time     : 2024/11/10 15:28
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Manager(Employee):
    bonus = None

    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理：{self.name} 工作中....")


class CommonEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def work(self):
        print(f"普通员工：{self.name} 工作中....")


manager = Manager("tom", '001', 20000, 15000)
employee = CommonEmployee("ming", "156", 10000)
manager.work()
employee.work()
