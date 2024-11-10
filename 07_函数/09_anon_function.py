# @Version  : 1.0
# @Author   : mmh
# @File     : 09_anon_function.py
# @Time     : 2024/11/2 13:25
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# 编写一个函数，可以接受一个匿名函数和两个数，通过匿名函数计算
# 返回两个数的最大值

def get_max(fun, num1, num2):
    """
    调用fun，返回num1,num2的最大值
    :param fun: 匿名接收函数
    :param num1: 参数1
    :param num2: 参数2
    :return:
    """
    return fun(num1, num2)


# 匿名函数调用
"""
    1.lambda x, y: x if x > y else y就是匿名函数
    2.没有返回值，计算结果就是返回值
"""
max_value=get_max(lambda x, y: x if x > y else y, 10, 20)
print(max_value)
