# @Version  : 1.0
# @Author   : mmh
# @File     : 10_全局变量和局部变量.py
# @Time     : 2024/11/2 13:44

# n1就是全局变量
n1 = 200


def f1():
    # n2就是局部变量
    n2 = 100
    print(n2)
    # 可以访问全局变量
    print(n1)


f1()
print(n1)

#不能访问局部变量n2
# print(n2)