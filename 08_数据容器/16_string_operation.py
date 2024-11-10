# @Version  : 1.0
# @Author   : mmh
# @File     : 16_string_operation.py
# @Time     : 2024/11/4 15:36
# 演示字符串中常用操作
str_name = "   jack tom mary hsp nono tom"
# len(str):字符串的长度，也就是包括多少个字符
print(f"{str_name}有{len(str_name)}个字符")

# str.replace(old,new[,count]):返回字符串的副本，其中出现的所有子字符串old都将替换成new
# 如果给出了可选参数count，则只替换前count次出现
# 返回字符串，并不会改变原来的字符串，而且返回一个新的字符串
str_name_new = str_name.replace("jack", "杰克", 1)
print("替换后的新字符串为：", str_name_new)

# str.split(sep=None,max split=-1)
# 返回一个有字符串单词组成的列表，使用sep作为分割字符串，如果给出了max split，
# 则最多进行 max split 次拆分（因此，列表最多会有 maxsplit+1 个元素）。如果max split
# 未指定或为-1，则不限制拆分次数（进行所有可能的拆分）

str_name_split = str_name.split(sep=" ", maxsplit=-1)
print(str_name_split)

# str.count(sub):统计指定字符串在字符串中出现的次数
# 统计tom在字符串出现了几次
print("tom在字符串中出现了几次：", str_name.count("tom"))

# str.index(sub):从字符串中找出指定字符串第一个匹配项的索引位置
print("str_name中找出指定字符串第一个匹配项的索引位置:", str_name.index("tom"))

# str.strip([chars]):返回原字符串的副本，移除其中的前导和末尾字符。chars为指定要移除字符的字符串
# 用这个方法可以去除前后的空格，或者去掉指定的某些字符
str_name_strip = str_name.strip(" ")
print(str_name_strip)
print("123tom123123".strip("123"))

# str.lower():返回原字符串小写的副本，不影响原来的字符
# 需求：将所有的字符串字母全部改成小些
str_names = "hskldjHPJKJKJ"
str_names_lower = str_names.lower()
print(f"转换成小写为：{str_names_lower}")

# str.upper():返回原字符串大写的副本，不影响原来的字符串
# 需求：全部字符串改成大写
str_names_upper = str_names.upper()
print(f"转换成大写为：{str_names_upper}")
