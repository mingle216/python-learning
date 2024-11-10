# @Version  : 1.0
# @Author   : mmh
# @File     : 08_list_exercise01.py
# @Time     : 2024/11/4 14:28

#循环从键盘输入5个成绩，保存到列表中，并输出
list1=[]
for _ in range(5):
    list1.append(float(input("请输入成绩：")))

print(list1)
