# @Version  : 1.0
# @Author   : mmh
# @File     : 01_bubble_sort.py
# @Time     : 2024/11/6 11:56
from enum import nonmember

# 可以使用sort方法实现排序功能，如下：
num_list = [24, 69, 96, 56, 13]
print("排序前".center(46, "="))
print(f"num_list:{num_list}")


# 使用sort方法完成序列
# num_list.sort()
# print("排序后".center(46,"="))
# print(f"num_list:{num_list}")

def bubble_sort(num_list):
    """
    功能：对传入的列表排序-顺序是从小到大
    :param num_list: 传入的列表
    :return: 无
    """
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print("冒泡排序-从小到大后".center(46, "="))
bubble_sort(num_list)
print(f"num_list:{num_list}")

def bubble_sort2(num_list):
    """
    功能：对传入的列表排序-顺序是从大到小
    :param num_list: 传入的列表
    :return: 无
    """
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            if num_list[j] < num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

bubble_sort2(num_list)
print("冒泡排序-从大到小后".center(46, "="))
print(f"num_list:{num_list}")