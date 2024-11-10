# @Version  : 1.0
# @Author   : mmh
# @File     : 07_float_detail.py
# @Time     : 2024/10/14 17:45
import decimal

n1 = 4.5
n2 = -6.8
print("n1:", n1)
print("n2:", n2)

n3 = 5.12
n4 = .512
print("n3:", n3)
print("n4:", n4)

# 科学计数法的形式：5.12e2 5.12E-2
n5 = 5.12e+2  # 5.12乘以10的二次方
n6 = 5.12E-2  # 5.12除以10的二次方
print("n5:", n5)
print("n6:", n6)

# 浮点类型计算后，存在精度损失，可以使用Decimal 类进行精确计算
# 如何解决？
# 1.为了避免浮点数的精度问题，可以使用Decimal 类进行精确计算
# 2.如果使用Decimal 类，需要导入Decimal 类
print(8.1 / 3)  # 2.6999999999999997

# 导入Decimal 类
from decimal import Decimal

print(Decimal('8.1') / Decimal('3'))  # 2.7
