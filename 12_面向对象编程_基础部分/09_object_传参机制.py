# @Version  : 1.0
# @Author   : mmh
# @File     : 09_object_传参机制.py
# @Time     : 2024/11/8 15:32
class Person:
    name = None
    age = None


# 测试对象作为参数传递到函数/方法的机制
def f1(person):
    print(f"2.person的地址：{id(person)}")
    person.name = "james"
    person.age += 1


p1 = Person()
p1.name = "jordan"
p1.age = 21

print(f"1.p1的地址：{id(p1)} p1.name:{p1.name} p1.age:{p1.age}")
f1(p1)
print(f"3.p1的地址：{id(p1)} p1.name:{p1.name} p1.age:{p1.age}")
