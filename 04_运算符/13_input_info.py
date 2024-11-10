# @Version  : 1.0
# @Author   : mmh
# @File     : 13_input_info.py
# @Time     : 2024/10/15 21:35

#要求：可以从控制台接收用户信息
name =input("请输入姓名：")
age =int(input("请输入年龄："))
score =input("请输入成绩：")

print("输入的信息如下：")
print("name:",name)
print("age:",age)
print("score:",score)

#注意，接收到的数据类型是str
print(type(name))


#如果我们希望对这个输入值进行算术运算，我们需要类型转换
print(float(age)+20)
print("==============")
#可以在接收数据的时候，直接转成需要的数据类型
# age =int(input("请输入年龄："))
print(type(age))