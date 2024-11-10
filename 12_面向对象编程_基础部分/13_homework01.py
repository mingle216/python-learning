# @Version  : 1.0
# @Author   : mmh
# @File     : 13_homework01.py
# @Time     : 2024/11/8 16:23

class A01:

    def max(self, list):
        # list=[1.1,2.9,-1.9,67.9]
        return max(list)


a = A01()
print(f"最大值为：{a.max([1.1,2.9,-1.9,67.9])}")
