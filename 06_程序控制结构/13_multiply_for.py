# @Version  : 1.0
# @Author   : mmh
# @File     : 13_multiply_for.py
# @Time     : 2024/10/16 15:28

# for i in range(2):
#     for j in range(3):
#         print(f"i={i} j={j}")

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#         if j==i:
#             print("\n")
# 打印金字塔
# for i in range(5):
#     for k in range(4 - i):
#         print(" ", end=" ")
#     for j in range((i + 1) * 2 - 1):
#         print("*", end=" ")
#     print("")
# 打印空心金字塔
# for i in range(1,6):
#     for k in range(5 - i):
#         print(" ", end=" ")
#     for n in range(i * 2 - 1):
#         if n==0 or n==(i-1)*2 or i==5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# 打印实心菱形，方法1:
# for i in range(1, 6):
#     for k in range(5 - i):
#         print(" ", end=" ")
#     for j in range(i * 2 - 1):
#         print("*", end=" ")
#     print("")
# for i in range(1, 6):
#     for k in range(i):
#         print(" ", end=" ")
#     for j in range(9-(2*i)):
#         print("*", end=" ")
#     print("")

# 打印实心菱形，方法2：
# for i in range(1,10):
#     if i<=5:
#         for k in range(5 - i):
#             print(" ", end=" ")
#         for j in range(i * 2 - 1):
#             print("*", end=" ")
#         print("")
#     else:
#         for k in range(i-5):
#             print(" ", end=" ")
#         for j in range(9-(2*(i-5))):
#             print("*", end=" ")
#         print("")

# 打印空心菱形：
# row = 9
# for i in range(1,row+1):
#     if i<=5:
#         for k in range(5 - i):
#             print(" ", end=" ")
#         for j in range(i * 2 - 1):
#             if j==0 or j==i * 2 - 2:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print("")
#     else:
#         for k in range(i-5):
#             print(" ", end=" ")
#         for j in range(9-(2*(i-5))):
#             if j == 0 or j == 8-(2*(i-5)):
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print("")

# 打印空心金字塔
# for i in range(1, 6):
#     for k in range(5 - i):
#         print(" ", end=" ")
#     for n in range(i * 2 - 1):
#         if n == 0 or n == (i - 1) * 2 or i == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

#while循环实现，空心金字塔
i = 0
while i < 6:
    k = 0
    n = 0
    while k < 5 - i:
        print(" ", end=" ")
        k += 1
    while n < i * 2 - 1:
        if n == 0 or n == (i - 1) * 2 or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        n += 1
    print("")
    i += 1