# @Version  : 1.0
# @Author   : mmh
# @File     : 08_for_01.py
# @Time     : 2024/10/16 13:50

for i in [1,2,3,4,5]:
    print("123")

#1.生成一个【1，2，3，4，5】
r1 =range(1,6,1)
print(list(r1))
#2.生成一个[0,1,2,3,4,5]
r2=range(0,6)
print(list(r2))
#3.生成一个[1,3,5,7,9]
r3=range(1,10,2)
print(list(r3))
#4.使用for+rang方式输出10句"hello,python"
for i in range(10):
    print("hello,python")