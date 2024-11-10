# @Version  : 1.0
# @Author   : mmh
# @File     : 02_import_module.py
# @Time     : 2024/11/6 21:31
from idlelib.outwin import file_line_progs
# import math
# import random
# import math,random

# 得到一个数的绝对值
# print(math.fabs(-11.2))
# 从列表中随机返回一个元素
# print(random.choice(['apple', 'pear', 'banana']))

# from 模块 import 函数、类、变量....
# 解读：导入math模块的 fabs函数
# from math import fabs

# 返回 x 的绝对值
# print(fabs(-11.6))

# # 导入模块的全部功能
# from math import *
#
# # 返回 x 的绝对值
# print(fabs(-234.5))
# # 返回 x 的平方根
# print(sqrt(9))

# 给导入的模块或者功能取别名

# import 模块 as 别名
import random as r
# from 模块 import 函数、类、变量....as 别名
from math import fabs as fa

print(r.choice([100,200,600]))
print(fa(-900.4))
