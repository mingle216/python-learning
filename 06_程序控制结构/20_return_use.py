# @Version  : 1.0
# @Author   : mmh
# @File     : 20_return_use.py
# @Time     : 2024/10/31 21:56

def f1():
    for i in range(1,5):
        if i==3:
            return
        print("i=",i)
print("结束了for...")

#调用f1函数
f1()