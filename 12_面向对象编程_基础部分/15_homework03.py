# @Version  : 1.0
# @Author   : mmh
# @File     : 13_homework01.py
# @Time     : 2024/11/8 16:23
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def zc(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius


c = Circle(4)
print(c.zc(), c.area())
