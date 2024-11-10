# @Version  : 1.0
# @Author   : mmh
# @File     : 09_for_else.py
# @Time     : 2024/10/16 14:18

#for-else使用案例
# nums=[1,2,3]
for i in range(5):
    print(i,"你好，mmh")
    if i==2:
        break
else:
    print("程序结束")