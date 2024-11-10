# @Version  : 1.0
# @Author   : mmh
# @File     : 11_data_type.py
# @Time     : 2024/10/15 14:33

# 在运算的时候，数据类型会向高精度转换，float的精度高于int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4=", var4, "var4的类型：", type(var4))
var2 = var2+0.1
print("var2=", var2, "var4的类型：", type(var2))
