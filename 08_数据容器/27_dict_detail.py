# @Version  : 1.0
# @Author   : mmh
# @File     : 27_dict_detail.py
# @Time     : 2024/11/5 13:36

dict_a={
    "jack":[10,20,30],
    "mary":(10,20,"hello"),
    "nono":{"apple","pear"},
    "smith":"计算机老师",
    "周星驰":{
        "性别":"男",
        "age":18,
        "地址":"香港"
    }
}

print(f"dict_a:{dict_a} 类型:{type(dict_a)}")

# 字典不支持索引，所以字段只能使用for进行遍历
dict_b={'one':1,'two':2,'three':3}
print("------------------遍历方式1------------------")
for key in dict_b:
    print(f"{key}:{dict_b[key]}")
print("------------------遍历方式2------------------")
for value in dict_b.values():
    print(value)
print("------------------遍历方式3------------------")
for key,value in dict_b.items():
    print(f"{key}:{value}")

# 创建空字典可以通过{},或者dict()
dict_c={}
dict_d=dict()
print(f"dict_c:{dict_c} 类型：{type(dict_c)}")
print(f"dict_d:{dict_d} 类型：{type(dict_d)}")