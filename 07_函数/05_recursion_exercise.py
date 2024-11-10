# @Version  : 1.0
# @Author   : mmh
# @File     : 05_recursion_exercise.py
# @Time     : 2024/11/1 17:44

# def add(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return add(n - 1) + add(n - 2)
#
# print(add(int(input("请输入一个整数："))))

# def peach_count(day):
#     if day == 10:
#         return 1  # 第10天剩余的桃子数量
#     else:
#         return (peach_count(day + 1) + 1) * 2
#
# # 调用函数，计算第1天的桃子数量
# print("最初共有桃子数量：", peach_count(1))

def result(n):
    if n == 1:
        return 3
    else:
        return 2*result(n-1)+1
print(result(10))