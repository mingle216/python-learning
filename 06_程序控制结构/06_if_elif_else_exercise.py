# @Version  : 1.0
# @Author   : mmh
# @File     : 06_if_elif_else_exercise.py
# @Time     : 2024/10/16 13:08


high = int(input("请输入男生身高："))
rich = int(input("请输入财富水平："))
handsome = input("是否帅气：")
if handsome == "是":
    handsome = True
else:
    handsome = False
if high > 180 and rich > 1000 and handsome:
    print("必须嫁")
elif high > 180 or rich > 1000 or handsome:
    print("比上不足，比下有余，嫁吧")
else:
    print("不嫁！")
