# @Version  : 1.0
# @Author   : mmh
# @File     : 14_tuple_exercise.py
# @Time     : 2024/11/4 15:13

tuple_a=('大话西游','周星驰',80,['周星驰','小甜甜'])

print("查询票价对应的索引为：",tuple_a.index(80))

for i in tuple_a[3]:
    print(f"演员为：{i}")

del tuple_a[3][1]
print(f"删除'小甜甜'后的元组为：{tuple_a}")
tuple_a[3].append('牛魔王')
tuple_a[3].append('猪八戒')
print(f"增加演员后为：{tuple_a[3]}")