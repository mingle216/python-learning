# @Version  : 1.0
# @Author   : mmh
# @File     : 02_compare_operator.py
# @Time     : 2024/10/15 15:47

# 案例
a = 9
b = 8
print(a > b)  # true
print(a >= b)  # true
print(a <= b)  # false
print(a < b)  # false
print(a == b)  # false
print(a != b)  # true
flag = a > b  # false
print("flag = ", flag)  # flag = ture
print(a is b)  # false
print(a is not b)  # true

print("------------------")
str1 = "abc#"
str2 = "abc#"
print(str1 is str2)  # true
