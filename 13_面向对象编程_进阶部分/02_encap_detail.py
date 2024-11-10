# @Version  : 1.0
# @Author   : mmh
# @File     : 02_encap_detail.py
# @Time     : 2024/11/9 11:57
class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    def get_job(self):
        return self.__job


clerk = Clerk("tom", "python工程师", 10000)
# 如果这样使用是，因为Python语言的动态特性，会动态的创建属性__job，但是这个属性
# 和我们在类中定义的属性__job 并不是同一个变量，我们在类中定义的__job 私有属性完整的名字是_Clerk__job
clerk.__job = "go工程师"
print(f"job={clerk.__job}")
print("ok")

# 获取真正的私有属性__job
print(f"{clerk.get_job()}")