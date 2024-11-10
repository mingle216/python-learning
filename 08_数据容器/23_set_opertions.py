# @Version  : 1.0
# @Author   : mmh
# @File     : 23_set_opertions.py
# @Time     : 2024/11/4 21:30

# 演示集合常用操作
# 定义集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 1.len():集合元素个数
print(f"集合元素个数为：{len(basket)}")

# 2.x in s :检测 x 是否是 s 中的成员
print(f"apple是否在集合中：{'apple' in basket}")

# 3.add(elem):将元素elem添加到集合中
basket.add('red')
print(f"将元素添加到集合后：{basket}")

# 4.remove(elem):从集合中移除元素elem
# 如果elem不存在集合中则会引发 KeyError
basket.remove('red')
print(f"将red从集合中移除：{basket}")

# 5.pop():从集合中移除并返回任意一个元素
# 如何元素为空则会引发KeyError
ele = basket.pop()
print({ele})
# pop() 操作会影响到原集合
print(f"pop后的集合为：{basket}")

# 6.union(*others):返回一个新集合
# 其中包括来自原集合以及 others 指定的所有集合中的元素
books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}
books_new = books.union(books_2)
books_new1 = books | books_2
print(f"将books和books_2进行并集操作：{books_new}")

# 7. intersection(*others):返回一个新集合
# 其中包含原集合以及 others 指定的所有集合中共有的元素
books_new2 = books.intersection(books_2)
books_new4 = books & books_2
print("book_4->", books_new2)
print("book_4->", books_new4)

# 8. difference(*others):返回一个新集合
# 其中包含原集合中在 others 指定的其他集合中不存在的元素
# 也就是:set - other - ...

# 求只存在books中的元素
books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}
books_5 = books.difference(books_2)
books_6 = books - books_2
print(books_5)

# 求只存在books_2中的元素
books7=books_2-books
print(books7)