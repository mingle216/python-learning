# @Version  : 1.0
# @Author   : mmh
# @File     : 08_bool_detail.py
# @Time     : 2024/10/14 19:28

num1 = 100
num2 = 200
print("num1>num2:", num1 > num2)

result = num1 > num2
print("result:", result)

# 查看result的数据类型
print("result的类型:", type(result))
print(type(1 > -1))

# 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时：
# Python 会将 True 视为 1，False 视为 0
b1 = False
b2 = True
print(b1 + 10)  # 10
print(b2 + 10)  # 11

# 说明：
# b1==0:表示赋值，把0赋给b1
# b1==0:表示判断，b1是否和0相等
if b1 == 0:
    print("ok")
if b2 == 1:
    print("hi")

# 在Python中，非0被视为真值，0被视为假值
if 0:
    print("哈哈")
if 1.1:
    print("嘻嘻")
if "mmh":
    print("mmh is very good!")