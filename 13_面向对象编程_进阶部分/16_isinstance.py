# @Version  : 1.0
# @Author   : mmh
# @File     : 16_isinstance.py
# @Time     : 2024/11/10 10:26

class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


obj = BB()
obj2 = AA()

# 分析输出的结果
print(f"obj 是不是BB的对象 {isinstance(obj, BB)}")
print(f"obj 是不是AA的对象 {isinstance(obj, AA)}")
print(f"obj 是不是CC的对象 {isinstance(obj, CC)}")

num = 9  # int 类型
print(f"num 是不是int：{isinstance(num, int)}")
print(f"num 是不是str：{isinstance(num, str)}")
# 只要是元组中的一个，就返回True
print(f"num 是不是str/int/list：{isinstance(num, (int, str, list))}")
