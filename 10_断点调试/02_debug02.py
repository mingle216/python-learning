# @Version  : 1.0
# @Author   : mmh
# @File     : 02_debug02.py
# @Time     : 2024/11/6 16:50
names_list = ["jordan", "kobe", "james", "messi"]
i = 0
# debug list 索引越界
while i <= len(names_list):
    print(f"names_list[i]: {names_list[i]}")
    i += 1
