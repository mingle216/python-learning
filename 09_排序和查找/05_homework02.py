import random

# 生成随机整数
list_a = [random.randint(1, 10) for _ in range(10)]

# 冒泡排序函数
def bubble_sort(list_a):
    for i in range(len(list_a) - 1):
        for j in range(len(list_a) - i - 1):
            if list_a[j] < list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

# 排序列表
bubble_sort(list_a)
print("排序后的列表:", list_a)

# 修正后的二分查找函数
def binary_search(find_val, list_a):
    left_index, right_index = 0, len(list_a) - 1
    find_index = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if list_a[mid_index] == find_val:
            # 找到一个8，记录下标
            find_index.append(mid_index)
            # 向左、向右扩展查找其他的8
            left, right = mid_index - 1, mid_index + 1
            while left >= 0 and list_a[left] == find_val:
                find_index.append(left)
                left -= 1
            while right < len(list_a) and list_a[right] == find_val:
                find_index.append(right)
                right += 1
            break  # 找到并扩展完成后退出
        elif list_a[mid_index] > find_val:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return sorted(find_index) if find_index else -1

# 调用二分查找
res = binary_search(8, list_a)
print("8的下标位置:", res)
