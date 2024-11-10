# @Version  : 1.0
# @Author   : mmh
# @File     : 17_break_detail.py
# @Time     : 2024/10/31 20:54
from tkinter.ttk import Treeview

count=0
while True:
    print("hi while")
    count = count + 1
    if count == 3:
        break
    while True:
        print("ok while")
        break
else:
    print("Hello,while")