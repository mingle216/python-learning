# @Version  : 1.0
# @Author   : mmh
# @File     : 20_class_object.py
# @Time     : 2024/11/10 14:47
# 下一个断点，可以看到Monster的情况
class Monster:
    name = "孙悟空"
    age = 100
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print(f"hi~{self.name}")

print(Monster)
print(f"Monster name: {Monster.name}  Monster age: {Monster.age}")

# 通过类名调用非静态成员方法
Monster.hi(Monster)

print("*"*32)