# @Version  : 1.0
# @Author   : mmh
# @File     : 11_func_type_hint.py
# @Time     : 2024/11/9 19:04

# 函数/方法的类型注解
# 给形参 name 进行注解，必须为string类型的参数，不然会警告错误
def fun1(name: str):
    for ele in name:
        print(ele)


fun1("mmh")


# 接收两个整数，返回整数
# 1.a:int ,b:int :对形参a,和b进行类型注解，标注a,b的类型为int
# 2.-> int 对返回值进行类型注解，标注返回值的类型为int
def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果是：{fun2(1, 2)}")
