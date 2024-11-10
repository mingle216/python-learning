# @Version  : 1.0
# @Author   : mmh
# @File     : 06_list_operation.py
# @Time     : 2024/11/4 10:15
# 演示列表常用操作
list_a = [100, 200, 300, 400, 600]
print("list_a列表元素个数：", len(list_a))
print("list_a列表最大元素：", max(list_a))
print("list_a列表最小元素：", min(list_a))

# list.append(obj):在列表末尾添加新的对象
# 请在list_a列表后，添加900
list_a.append(900)
print("list_a:", list_a)

# list.count(obj):统计某个元素在列表中出现的次数
print(list_a.count(100))

# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list_b = [1, 2, 3]
# 将list_b追加到list_a中
list.extend(list_a, list_b)
print("list_a:", list_a)

# list.index(obj):从列表中找出某个值第一个匹配项的索引位置
# 如果找不到，会报错：valueError
print("300第1次出现在序列中的索引是：", list_a.index(300))

# 翻转list_a,list_a.reverse()
list_a.reverse()
print("翻转后的list_a:", list_a)

# list.insert(index,obj):将对象插入列表指定的index位置
# 请实现把666插入到index为1的位置

list_a.insert(1,666)
print("list_a:", list_a)
