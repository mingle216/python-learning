# @Version  : 1.0
# @Author   : mmh
# @File     : 16_break_random.py
# @Time     : 2024/10/31 20:40
import random

# 随机生成1-100个数，直到生成97这个数，看看你用了多少次？
num = 0
toiler= 1
# while num != 97:
#     print(f"{num}不是97！")
#     num = random.randrange(1, 100)
#     toiler += 1
# print(f"一共用了{toiler}次")

while True:
    num = random.randint(1, 100)
    if num == 97:
        break
    toiler+=1
    print(f"{num}不是97！")
print(f"一共用了{toiler}次")