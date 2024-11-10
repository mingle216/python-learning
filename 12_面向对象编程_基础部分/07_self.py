# @Version  : 1.0
# @Author   : mmh
# @File     : 07_self.py
# @Time     : 2024/11/8 14:52
# class Dog:
#     name = "波斯猫"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息：{name}")
#         # 如果希望访问到属性name,使用self.name
#         print(f"成员变量name:{self.name}")
#
#     # 静态方法
#     # 1.通过@staticmethod 可以将方法转为静态方法
#     # 2.如果是一个静态方法，可以不带self
#     # 3.静态的方法的调用形式有变化
#     @staticmethod
#     def ok():
#         print("ok....")


# dog = Dog()
# dog.info("加菲猫")
# # 静态方法调用方法一：
# dog.ok()
# # 静态方法调用方法二：
# Dog.ok()

# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def hi(self):
#         print(f"hi self:{id(self)}")


# # self表示当前对象本身
# # 创建对象dog2
# dog2 = Dog()
# print(f"dog2:{id(dog2)}")
# dog2.hi()
# # 创建对象dog3
# print("------------------------")
# dog3 = Dog()
# print(f"dog3:{id(dog3)}")
# dog3.hi()

# 在方法内部，要访问成员变量和成员方法，需要使用self
class Dog:
    name = "藏獒"
    age = 2

    def eat(self):
        print(f"{self.name} 饿了!")

    def cry(self, name):
        print(f"{name} is crying")
        print(f"{self.name} is crying")
        self.eat()
        # 不能直接调用
        # eat()

dog = Dog()
# 修改 dog 对象的属性name => 中华田园犬
dog.name="中华田园犬"
dog.cry("金毛")