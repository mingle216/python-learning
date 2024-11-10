# @Version  : 1.0
# @Author   : mmh
# @File     : 13_type_change_detail.py
# @Time     : 2024/10/15 14:49

# 显示类型转换注意事项

# 不管什么值的int,floot都可以转成str，str(x)将对象x转为字符串

n1 = 100
n2 = 126.65
print(str(n1))
print(str(n2))

# int转成float，会增加小数部分，比如123->123.0
# float转成int时，会去掉小数部分，比如123.65->123

print(float(n1))  # 100.0
print(float(n2))  # 123

n3 = "12.3"
# print(float(n3))
# print(int(n3))

# 在将str类型转成基本数据类型时，要确保str值能够转成有效的数据
n4 = "hello"
# print(float(n4))
# print(int(n4))
