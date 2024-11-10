# @Version  : 1.0
# @Author   : mmh
# @File     : 12_union_type_hint.py
# @Time     : 2024/11/9 19:14
from typing import Union

# 联合类型注解，a 可以是int或者str
a: Union[int, str] = 100

# my_list是list类型，元素可以是int或者str类型都行
my_list: list[Union[int, str]] = [100, 200, 300, "tim"]


# 函数/方法使用联合类型注解：
# 接收两个数 (可以是int/float)，返回（int/float）
def cal(num1: Union[int, float],
        num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

print(f"结果是：{cal(10,20.2)}")