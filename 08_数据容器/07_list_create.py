# @Version  : 1.0
# @Author   : mmh
# @File     : 07_list_create.py
# @Time     : 2024/11/4 10:57

lst1 = [ele * 2 for ele in range(1, 5)]
print(lst1)

lst2 = [ele + ele for ele in "韩顺铂"]
print(lst2)

# 要求生成一个列表，内容为[1,4,9,16,25,36,49,64,81,100]
lst3 = [ele * ele for ele in range(1, 11)]
print(lst3)
