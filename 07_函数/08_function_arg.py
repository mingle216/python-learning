# @Version  : 1.0
# @Author   : mmh
# @File     : 08_function_arg.py
# @Time     : 2024/11/2 11:16

#f3接收多个函数作为参数传入
def f3(my_fun,num1,num2,my_fun2):
    return my_fun(num1,num2),my_fun2(num1,num2)

#定义一个函数，可以返回两个数的最大值
def get_max_val(num1,num2):
    max_val = num1 if num1>num2 else num2
    return max_val
#定义函数，可以返回两个数的和
def get_sum(num1,num2):
    return num1+num2
x,y=f3(get_max_val,3,40,get_sum)
print(f"两数最大值：{x},两数和为：{y}")