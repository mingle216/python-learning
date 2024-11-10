# @Version  : 1.0
# @Author   : mmh
# @File     : 15_master_feed_animal.py
# @Time     : 2024/11/10 10:15

# 说明：使用多态的方式完成
class Food:
    name = None

    def __init__(self, name):
        self.name = name


class Fish(Food):
    # 特有的属性和方法
    pass


class Bone(Food):
    # 特有的属性和方法
    pass


class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass

class Master:
    name = None
    def __init__(self, name):
        self.name = name

    def feed(self,animal: Animal,food: Food):
        print(f"主人：{self.name} 给{animal.name} 喂{food.name}")

cat = Cat("咪咪")
dog = Dog("大黄")
fish = Fish("黄花鱼")
bone = Bone("牛骨")
master = Master("ming")
master.feed(cat,fish)
master.feed(dog,bone)
