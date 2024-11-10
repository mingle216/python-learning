# @Version  : 1.0
# @Author   : mmh
# @File     : 19_slice_use.py
# @Time     : 2024/11/4 17:57

# 对字符串进行切片
str = "hello,world"

# 需求：截取"hello"
str_slice = str[0:5:1]
print("str_slice:", str_slice)

# 对列表进行切片
list_a = ["jack", "tom", "yoyo", "nono", "hsp"]
# 需求：截取["tom","nono"]
print(list_a[1:4:2])

# 对元组进行切片
tuple_a = (100, 200, 300, 400, 500, 600)
print(tuple_a[1:5:1])
