# @Version  : 1.0
# @Author   : mmh
# @File     : 01_encap_quick_start.py
# @Time     : 2024/11/9 11:25

class Clerk:
    name = None
    __job = None
    __salary = None

    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共的方法，对私有属性操作（根据实际的业务编写）
    # 给私有属性__job进行赋值
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    # 私有方法
    def __hi(self):
        print("调用私有方法hi()")

    # 提供公共方法，操作私有方法
    def f1(self):
        self.__hi()


clerk = Clerk("tom","python工程师",10000)
# 如果是公共属性，在类的外部可以直接访问
print(clerk.name)
# 如果是私有属性，在类的外部不可以直接访问
# AttributeError:'Clerk' object has no attribute '__job'
# print(clerk.__job)
print(clerk.get_job())
clerk.set_job("java工程师")
print(clerk.get_job())

# 私有方法不能在类的外部直接调用
# clerk.__hi()

# 通过公共方法，调用私有方法
clerk.f1()

