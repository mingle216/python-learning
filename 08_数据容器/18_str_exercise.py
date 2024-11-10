# @Version  : 1.0
# @Author   : mmh
# @File     : 18_str_exercise.py
# @Time     : 2024/11/4 16:09

# 定义一个字符串，str_names="tom jack mary nono smith hsp"
# 统计一共有多少个人名

str_names = "tom jack mary nono smith hsp"
print(f"一共有{len(str_names)}个人名")

str_names_new = str_names.replace("hsp", "老汉")
print(f"修改后的人名为：", str_names_new)

str_names_upper = str_names[0].upper() + str_names[1:]
print(f"首字母改成大写为：{str_names_upper}")
# 将首字母改为大写str.capitalize
str_names_one = str_names.capitalize()
print(f"首字母改成大写为：{str_names_one}")

# 遍历字符串，如果是英文则首字母大写
print("=====================")
# ['tom', 'jack', 'mary', 'nono', 'smith', '老汉']
# 先拆分字符串，再使用函数
str_names_list = str_names_new.split(" ")
print(str_names_list)
str_names_upper = ""
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize() + "｜"
# 去掉两遍的“ ”
str_names_upper = str_names_upper.strip("｜")
print(str_names_upper)
