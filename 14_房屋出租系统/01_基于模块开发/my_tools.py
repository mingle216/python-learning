# @Version  : 1.0
# @Author   : mmh
# @File     : my_tools.py
# @Time     : 2024/11/15 16:07


def read_confirm_select():
    """
    判断选择是否是y/n,如果不是就会一直输入
    :return:
    """
    print("请输入你的选择(Y/N),请确认选择:",end="")
    while True:
        key=input()
        if key.upper()=='N' or key.upper()=='Y':
            break
        else:
            print("输入信息错误，请重新输入....")

    return key.upper()