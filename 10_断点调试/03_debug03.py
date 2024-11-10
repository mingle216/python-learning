# @Version  : 1.0
# @Author   : mmh
# @File     : 03_debug03.py
# @Time     : 2024/11/6 17:04

def f2(num):
    res = 0
    for i in range(num):
        res += i
    return res


s = f2(5)
print(s)

def f1(name):
    print(f"{name}111111")
    print(f"{name}111111")
    print(f"{name}111111")
    print(f"{name}111111")
    print(f"{name}111111")
    f2(9)
    print(f"{name}111111")

f1('mm')
