# @Version  : 1.0
# @Author   : mmh
# @File     : 05_hens_question.py
# @Time     : 2024/11/2 18:04

all_weight=[3,5,1,3.4,2,50]
sum =0
for w in all_weight:
    sum+=w
print(f"六只鸡的总体重为：{sum}，平均体重为：{round(sum/len(all_weight),2)}")

list1=[1,2.1,'hmm']
print(list1[-1])
print(list1[-2])
#不能索引越界
# print(list1[-4])