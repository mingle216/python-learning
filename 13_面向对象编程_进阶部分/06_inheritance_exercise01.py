# @Version  : 1.0
# @Author   : mmh
# @File     : 06_inheritance_exercise01.py
# @Time     : 2024/11/9 14:35
class GrandPa:
    name="大头爷爷"
    hobby="旅游"

class Father(GrandPa):
    name = "大头爸爸"
    age = 39

class Son(Father):
    name = "大头儿子"

son = Son()
print(f"son.name={son.name} son.age={son.age} son.hobby={son.hobby}") #son.name=大头儿子 son.age=39 son.hobby=旅游