# @Version  : 1.0
# @Author   : mmh
# @File     : 05_method_example.py
# @Time     : 2024/11/8 12:50

class Person:
    name = None
    age = None

    def hi(self):
        print("hi~python")

    def cal01(self):
        cal_sum = 0
        for i in range(1,1001):
            cal_sum += i
        return cal_sum

    def cal02(self,n):
        cal_sum = 0
        for i in range(1,n+1):
            cal_sum += i
        return cal_sum

    def get_sum(self,n1,n2):
        return n1+n2

p1 = Person()
p1.hi()
print(p1.cal01())
print(p1.cal02(10))
print(p1.get_sum(1,2))
