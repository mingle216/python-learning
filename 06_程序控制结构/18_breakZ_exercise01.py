# @Version  : 1.0
# @Author   : mmh
# @File     : 18_breakZ_exercise01.py
# @Time     : 2024/10/31 21:04

# 1-100以内的数求和，求出当和第一次大于20的当前控制循环的变量值是多少？
all_num=0
for i in range(1,101):
    all_num+=i
    if all_num > 20 :
        print(i)
        break