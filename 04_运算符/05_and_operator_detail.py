# @Version  : 1.0
# @Author   : mmh
# @File     : 05_and_operator_detail.py
# @Time     : 2024/10/15 16:07

# 案例：
a = 1
b = 99
print(a and b)  # 99
print((a > b) and b)  # false
print((a < b) and b)  # 99

# 细节案例
a = 1
b = 99
print(a or b)  # 1
print((a > b) or b)  # 99
print((a < b) or b)  # true
