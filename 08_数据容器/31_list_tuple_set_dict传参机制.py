# @Version  : 1.0
# @Author   : mmh
# @File     : 31_list_tuple_set_dict传参机制.py
# @Time     : 2024/11/6 10:59

# ----------------------list----------------------
def f1(my_list):
    print(f"f1() my_list:{my_list} 地址是：{id(my_list)}")
    my_list[0] = 'jack'
    print(f"f1() my_List:{my_list} 地址是{id(my_list)}")


# 测试
my_list=["tom","mary","mmh"]
print(f"f1() my_List:{my_list} 地址是{id(my_list)}")
f1(my_list)
print(f"f1() my_List:{my_list} 地址是{id(my_list)}")
# ----------------------list----------------------
# ----------------------list----------------------
# ----------------------list----------------------
