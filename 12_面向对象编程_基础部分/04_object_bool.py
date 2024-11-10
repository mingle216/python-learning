# @Version  : 1.0
# @Author   : mmh
# @File     : 04_object_bool.py
# @Time     : 2024/11/8 12:38
print("--------下面对象的布尔值为false--------")
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool({}))
print(bool())

# 所有对象都有一个布尔值，有些代码直接使用对象的布尔值做判断
print("字符串判断布尔值".center(46, '-'))
content = "hello"
if content:
    print(f"hi {content}")
else:
    print("空字符串")

print("列表判断布尔值".center(46, '-'))
lst = [1, 2, 3]
if lst:
    print(f"lst: {lst}")
else:
    print("空列表")
