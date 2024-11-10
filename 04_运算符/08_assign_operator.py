# @Version  : 1.0
# @Author   : mmh
# @File     : 08_assign_operator.py
# @Time     : 2024/10/15 16:27

# 赋值运算符案例
num1 = 10
i = 100
i += 100
print("i=", i)
i -= 100
print("i=", i)
i *= 2
print("i=", i)

# /= //= %= 等等

# 赋值交换
a = 10
b = 20
print(f"没交换前 a={a},b={b}")
print("--------------------")
t = a
a = b
b = t
print(f"交换后 a={a},b={b}")
print("====================")
# 另一种简单的变量交换
# x , y = y , x
a,b=b,a
print(f"交换后 a={a},b={b}")