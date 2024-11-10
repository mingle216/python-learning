# @Version  : 1.0
# @Author   : mmh
# @File     : 22_abstract_class_quick_start.py
# @Time     : 2024/11/10 15:01
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这时cry就是一个抽象方法
    @abstractmethod
    def cry(self):
        """
        动物都有叫的行为，，但是这个行为不明确（不能明确的实现..）
        """
        # print("不知道是什么动物，不知道是什么叫声...")
        pass


# 注意：抽象类(含有实例方法)是不能实例化的
# TypeError: Can't instantiate abstract class Animal
# animal = Animal("mimi",2)

# 编写一个子类Tiger，继承Animal 并实现抽象方法
class Tiger(Animal):
    def cry(self):
        print(f"老虎{self.name} 嗷嗷叫...")
tiger = Tiger("mimi",2)
tiger.cry()