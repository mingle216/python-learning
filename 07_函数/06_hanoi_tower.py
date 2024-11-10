# @Version  : 1.0
# @Author   : mmh
# @File     : 06_hanoi_tower.py
# @Time     : 2024/11/2 10:39

def hanoi_tower(num,a,b,c):
    if num == 1:
        print("第1个盘从：",a,"->",c)
    else:
        hanoi_tower(num-1,a,b,c)
        print(f"第{num}个盘从： {a} -> {c}")
        hanoi_tower(num-1,b,a,c)

hanoi_tower(5,"a","b","c")