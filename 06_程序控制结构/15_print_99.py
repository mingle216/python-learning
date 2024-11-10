# @Version  : 1.0
# @Author   : mmh
# @File     : 15_print_99.py
# @Time     : 2024/10/31 20:34

#打印出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {i*j} ',end=' ')
    print("")