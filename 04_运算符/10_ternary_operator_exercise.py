# @Version  : 1.0
# @Author   : mmh
# @File     : 10_ternary_operator_exercise.py
# @Time     : 2024/10/15 20:04

# 使用前面讲的 if-else方式，得到3个数的最大值

a = 10000
b = 101
c = 999999

# m1 = a if a > b else b
# m2 = b if b > c else c
m1 = (a if a > b else b) if (a if a > b else b) > c else c
print(m1)
