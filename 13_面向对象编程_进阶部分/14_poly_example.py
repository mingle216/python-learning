# @Version  : 1.0
# @Author   : mmh
# @File     : 14_poly_example.py
# @Time     : 2024/11/9 19:42
# class Animal:
#     def cry(self):
#         pass
#
#
# class Cat(Animal):
#     def cry(self):
#         print("小猫 喵喵叫....")
#
#
# class Pig(Animal):
#     def cry(self):
#         print("小猪 噜噜叫....")
#
#
# class Dog(Animal):
#     def cry(self):
#         print("小狗 汪汪叫....")
#
# # 注意：在Python 面向对象编程中，子类对象可以传递给父类类型
# def func(animal: Animal):
#     print(f"animal 类型是{type(animal)}")
#     animal.cry()
#
#
# cat = Cat()
# dog = Dog()
# pig = Pig()
#
# # 调用函数
# func(cat)
# func(dog)
# func(pig)

class AA:
    def hi(self):
        print("AA-hi()...")


class BB:
    def hi(self):
        print("BB-hi()...")


def test(obj):
    obj.hi()


aa = AA()
bb = BB()
test(aa)
test(bb)
