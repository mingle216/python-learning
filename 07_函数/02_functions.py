# @Version  : 1.0
# @Author   : mmh
# @File     : 02_functions.py
# @Time     : 2024/11/1 10:38

# 自定义cry函数，输出“小猫，喵喵叫....”

def cry():
    print("小猫，喵喵叫....")


cry()
cry()
cry()


# 计算从1+....+1000的结果
def cal01():
    m1 = 0
    for i in range(1000):
        m1 += i
    return m1


print(cal01())


# 自定义cal02,函数可以接收一个数n，计算从1+++到n的结果
def cal02(a):
    m1 = 0
    for i in range(a):
        m1 += i
    return m1


print(cal02(1000))


# 自定义get_sum函数，可以计算两个数的和，并返回结果
def get_sum(a, b):
    return a + b


print(get_sum(1, 2))


# 使用函数解决前面的问题
def cc(n1, n2, fu):
    if fu == "+":
        return n1 + n2
    elif fu == "-":
        return n1 - n2
    elif fu == "*":
        return n1 * n2
    elif fu == "/":
        return n1 / n2
    else:
        return "输入错误，重新输入"

n1 = float(input("请输入第一个数："))
n2 = float(input("请输入第二个数："))
fu = input("请输入运算符 (+, -, *, /)：")
result = cc(n1, n2, fu)
print(f"{n1} {fu} {n2} = {result}")
