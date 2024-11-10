# @Version  : 1.0
# @Author   : mmh
# @File     : 28_dict_operations.py
# @Time     : 2024/11/5 13:54

# 演示字典的常用操作
# 1.len(d):返回字典中的d的个数
dict_a = {'one': 1, 'two': 2, "three": 3}
print("dict_a的元素个数是：", len(dict_a))

# 2.d[key]:返回d中以key为键的项。如果映射中不存在key则会引发keyError
print(f"key为three对应的value：{dict_a['three']}")

# 3.d[key] = value :将 d[key] 设为 value,如果key已经存在，则是修改value
# 如果key没有存在，则是增加key-value，注意会直接修改原来的字典-示意图
# 修改 需求：修改 key ='one' 对应的value为 第一
dict_a['three'] = 300
print(dict_a)
# 添加需求：增加key 为‘four’ value为4
dict_a['four'] = 4
print(f"dict_a:{dict_a}")

# 4.del_d[key]:将d[key] 从 d 中移除,如果key已经存在，则是修改value
del dict_a['four']
print(dict_a)

# 5.pop(key,[default])
# 如果key 存在于字典中则将其移除并返回其值，否则返回 default
# 如果default 未给出且key 不存在于字典中，则会引发keyError
# 将key 为‘1’的值返回，并将该元素从字典中移除
val = dict_a.pop('one')
print(val)
print(dict_a)

# 6. keys():返回字典中所有的key
dict_a_keys = dict_a.keys()
print(f"dict_a_keys:{dict_a_keys}")
for key in dict_a_keys:
    print("k->", key)

# 7. key in d:如果d 中存在键key 则返回 true，否则返回false
# 判断 字典中是否有 key 'two'
print('two' in dict_a)

# 8.clear():移除字典中所有的元素
dict_a.clear()
print(dict_a)
