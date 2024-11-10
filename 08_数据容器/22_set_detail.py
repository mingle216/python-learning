# @Version  : 1.0
# @Author   : mmh
# @File     : 22_set_detail.py
# @Time     : 2024/11/4 21:19

# 集合是由不重复元素组成的无序容器

# 不重复元素组成，可以理解成会自动去重
basket = {'apple', 'orange', 'pear', 'banana', 'orange', 'banana'}
print(f'{basket}')

# 无序,也就是你定义元素的顺序和取出的顺序不能保持一致
# 集合底层会按照自己的一套算法来存储和取数据，所以每次取出顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(set_a)
print(set_a)
print(set_a)

# 使用for对集合进行遍历
print("-" * 30)
basket = {'apple', 'orange', 'pear', 'banana','apple', 'orange','blue'}
for e in basket:
    print(e)
