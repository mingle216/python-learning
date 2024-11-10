# @Version  : 1.0
# @Author   : mmh
# @File     : 03_format_output.py
# @Time     : 2024/10/14 16:25

# 格式化输出案例
# 定义变量
age = 18
name = "林黛玉"
gender = '女'
score = 99.5# @Version  : 1.0
# @Author   : mmh
# @File     : 03_format_output.py
# @Time     : 2024/10/14 16:25

# 格式化输出案例
# 定义变量
age = 18
name = "林黛玉"
gender = '女'
score = 99.5

# % 操作符输出
print("个人信息：%s-%d-%s-%.2f" % (name, age, gender, score))

# format()函数
print("个人信息：{} {} {} {}".format(name, age, gender, score))

# f-string(推荐)
print(f"个人信息：{name} {age} {gender} {score}")


# % 操作符输出
print("个人信息：%s-%d-%s-%.2f" % (name, age, gender, score))

# format()函数
print("个人信息：{} {} {} {}".format(name, age, gender, score))

# f-string(推荐)
print(f"个人信息：{name} {age} {gender} {score}")
