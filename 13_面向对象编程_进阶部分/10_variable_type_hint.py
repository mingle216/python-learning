# @Version  : 1.0
# @Author   : mmh
# @File     : 10_variable_type_hint.py
# @Time     : 2024/11/9 18:51

"""
    1.n1:int: 对n1进行类型注解，标注n1的类型为int
    2.注意如果，给出的值的类型和标注的类型不一致，则Pycharm会给出黄色警告
"""
n1: int = 10
n2: float = 10.1
is_pass: bool = True
name: str = "mimi"


# 定义类Cat
class Cat:
    pass

# 对实例对象类型注解
# cat:Cat : 对cat进行类型注解，标注cat的类型是cat
cat: Cat = Cat()

#