# @Version  : 1.0
# @Author   : mmh
# @File     : 04_homework01.py
# @Time     : 2024/11/6 16:07
import random

# 1.随机生成10个整数，保存到列表中
list_a = []
for i in range(10):
    list_a.append(random.randint(1, 10))


# 2.使用冒泡排序,从大到小
def bubble_sort(list_a):
    for i in range(len(list_a) - 1):
        for j in range(len(list_a) - i - 1):
            if list_a[j] < list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

# 3.调用函数，输出列表
bubble_sort(list_a)
print(list_a)
