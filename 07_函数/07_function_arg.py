# @Version  : 1.0
# @Author   : mmh
# @File     : 07_function_arg.py
# @Time     : 2024/11/2 11:07

#定义一个函数，返回它的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val

def f1(fun, num1, num2):
    return fun(num1, num2)

def f2(fun, num1, num2):
    return num1 + num2, fun(num1, num2)

print(f1(get_max_val,10,40))
x,y = f2(get_max_val,50,40)
print(f"x={x} y={y}")
