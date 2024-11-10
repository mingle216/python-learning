# @Version  : 1.0
# @Author   : mmh
# @File     : 21_homework01.py
# @Time     : 2024/10/31 22:00

#有100000，每经过一次路口，需要交费，规则如下：
# 当现金>50000时，每次交5%
# 当现金<=50000时，每次交1000
#计算经过多少次路口，使用while+break完成

money = 100000
count = 0
# 当现金>50000时，每次交5%
# 当现金<=50000时，每次交1000
while True:
    if money > 50000:
        count +=1
        money -= money * 0.05
    elif money >1000:
        count += 1
        money -= 1000
    else:
        break
print(count,money)