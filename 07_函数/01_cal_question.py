# @Version  : 1.0
# @Author   : mmh
# @File     : 01_cal_question.py
# @Time     : 2024/11/1 10:23

#输入两个数，再输入一个运算符（+-*/）得到结果
n1=float(input("请输入第一个数："))
n2=float(input("请输入第二个数："))
fu=input("请输入运算符：")
if fu=="+":
    print(f"{n1}{fu}{n2}=",n1+n2)
elif fu=="-":
    print(f"{n1}{fu}{n2}=",n1-n2)
elif fu=="*":
    print(f"{n1}{fu}{n2}=",n1*n2)
elif fu=="/":
    print(f"{n1}{fu}{n2}=",n1/n2)
else:
    print("输入错误，重新输入")