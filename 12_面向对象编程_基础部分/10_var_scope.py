# @Version  : 1.0
# @Author   : mmh
# @File     : 10_var_scope.py
# @Time     : 2024/11/8 15:36
from tkinter.font import names


# class Cat:
#     name = None
#     age = None
#
#     def cal(self, n1, n2):
#         result = n1 + n2
#         print(f"result={result}")
#
#
# c = Cat()
# c.cal(1,2)

# class Cat():
#     # 属性的作用域在整个类中
#     name = None
#     age = None
#
#     # n1,n2,result 就是局部变量
#     def cal(self, n1, n2):
#         result = n1 + n2
#         print(f"result={result}")
#         print(f"cal()使用 属性name{self.name}")
#
#     def cry(self):
#         print(f"cry()使用 属性name{self.name}")
#
#     def eat(self):
#         print(f"eat()使用 属性name{self.name}")
#
#
# cat = Cat()
# cat.cal(10, 20)
# cat.cry()
# cat.eat()

class Cat():
    # 属性的作用域在整个类中
    name = None
    age = None

    def hi(self):
        name = "皮皮"
        print(f"name={name}")
        print(f"name={self.name}")


cat = Cat()
cat.name ="小咪"
print("--------------------------")
cat.hi()

