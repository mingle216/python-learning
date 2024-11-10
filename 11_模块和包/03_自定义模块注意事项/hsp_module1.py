# @Version  : 1.0
# @Author   : mmh
# @File     : hsp_module1.py
# @Time     : 2024/11/6 21:53

# 在hsp_module1.py 中，没有__all__时，会导入所有功能
# 使用__all__=["ok"] 在其他文件使用 from hsp_module1 import * 只会导入ok()
# 注意：import 模块 方式，不受__all__ 的限制

# 如果其他文件中使用的是from hsp_module1 import * 导入，则只能导入ok函数
__all__ = ["ok"]


def hi():
    print('hi')


def ok():
    print('ok')


if __name__ == '__main__':
    hi()
    ok()

# print("hsp_module1:",__name__)
