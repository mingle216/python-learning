# @Version  : 1.0
# @Author   : mmh
# @File     : 03_list_while.py
# @Time     : 2024/11/2 17:54

list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# list的个数
print(len(list_color))

index = 0
while index < len(list_color):
    print(f"数据中第{index+1}个元素为：", list_color[index])
    index += 1
