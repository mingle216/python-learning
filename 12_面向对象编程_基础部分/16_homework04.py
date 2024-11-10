# @Version  : 1.0
# @Author   : mmh
# @File     : 13_homework01.py
# @Time     : 2024/11/8 16:23
class Cal:

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def sum(self):
        return self.m + self.n

    def shang(self):
        if self.m != 0 and self.n != 0:
            return self.m / self.n
        else:
            print("除数不能为0！")
            return None

    def cha(self):
        return self.m - self.n

    def cheng(self):
        return self.m * self.n


c = Cal(10, 2)
print(f"和为：{c.sum()},差为：{c.cha()},乘为:{c.cheng()},商为：{c.shang()}")
