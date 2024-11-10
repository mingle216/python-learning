# @Version  : 1.0
# @Author   : mmh
# @File     : 04_if_exercise.py
# @Time     : 2024/10/16 12:43

# 定义两个整数变量并赋值，判断两数之和，如果大于等于50，打印：“hello,world”

a = 15
b = 56
if a + b >= 50:
    print("hello,world")

# 定义2个float型变量并赋值，如果第一个数大于10.0，且第2个数小于20.0，打印两数之和

a = float(56)
b = float(10)
if a > 10.0 and b < 20.0:
    print(f"{a}+{b}={a + b}")

# 定义两个变量int类型，判断两者的和，是否能被3又能被5整除，打印显示信息：
m1 = int(11)
m2 = int(5)
if (m1 + m2) % 3 == 0 and (m1 + m2) % 5 == 0:
    print(f"能被整除：{m1},{m2}")
else:
    print("不能被整除")

# 判断一个年份是否是闰年，闰年的条件是符合下面两者之一：
# 1.年份能被4整除，但不能被100整除
# 2.能被400整除
year=int(2014)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("全部符合，是闰年")
else:
    print("不是闰年")