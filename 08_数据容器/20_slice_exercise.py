# @Version  : 1.0
# @Author   : mmh
# @File     : 20_slice_exercise.py
# @Time     : 2024/11/4 18:12

list_name=["Jack","Lisa","Hsp","Paul","Smith","Kobe"]

print(list_name[:4:])
print(list_name[3:])

slice_b=list_name[-1:-4:-1]
slice_b.reverse()
print(slice_b)