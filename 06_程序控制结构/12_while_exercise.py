# @Version  : 1.0
# @Author   : mmh
# @File     : 12_while_exercise.py
# @Time     : 2024/10/16 14:57

# 打印1-100之间能被3整除的数
i = 1
while i <= 100:
    if i % 3 == 0:
        print(i, "能被3整除")
    i += 1

print("================")

# 打印40-200之间所有的偶数
n = 40
while n <= 200:
    if n % 2 == 0:
        print(n, "是偶数")
    n += 1

# 不断输入姓名，直到输入"exit"为止
# name=input("请输入你的姓名：")
# while name!="exit":
#     name = input("请输入你的姓名：")

# 打印1——100之间所有9的倍速的整数，统计个数以及总和
# num=1
# count=0
# sum=0
# while num <= 100:
#     if num % 9 == 0:
#         count +=1
#         sum += num
#         print(num,"是9的倍数")
#     num += 1
# print(f"sum = {sum}, count = {count}")

s = int(input("请输入一个整数："))
i = 0
while i < s:
    print(f"{i}+{s-i}={s}")
    i += 1
