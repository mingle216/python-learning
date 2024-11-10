# @Version  : 1.0
# @Author   : mmh
# @File     : 03_binary_search.py
# @Time     : 2024/11/6 15:54

# 二分查找
my_list = [1, 8, 10, 89, 95, 123, 64]
find_val = 158

my_list.sort()
print(my_list)


def binary_search(my_list, find_val):
    left_index, right_index = 0, len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] == find_val:
            find_index = mid_index
            break
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
        elif my_list[mid_index] > find_val:
            right_index = mid_index - 1
    return find_index


binary_search(my_list, find_val)
print(binary_search(my_list, find_val))
