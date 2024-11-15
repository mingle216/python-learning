# @Version  : 1.0
# @Author   : mmh
# @File     : main.py
# @Time     : 2024/11/12 21:12
"""
    说明：出租系统的主程序
"""
from curses.ascii import isdigit

from house_operation import *


def main():
    """
    这是主函数，也就是程序的执行入口
    :return:
    """
    while True:
        # 调用main_menu函数显示主菜单
        main_menu()
        # 判断输入是否为1到6之间的值
        while True:
            choose = input("请输入你的选择(1-6):")

            # 检查输入是否为数字
            if not choose.isdigit():
                print("输入无效，请输入数字！")
                continue

            # 将输入转换为整数并检查是否在1到6之间
            choose = int(choose)
            if 1 <= choose <= 6:
                print(f"你的选择是: {choose}")
                break
            else:
                print("输入的值不在1到6之间，请重新输入！")
                continue
        # 退出功能
        if choose == 6:
            if exit_menu() == -1:
                break
            elif choose == 1:
                main_menu()
        # 显示房屋列表
        elif choose == 5:
            show_info()
        # 增加房源
        elif choose == 1:
            add_house()
        # 删除房源
        elif choose == 3:
            delete_house()
        # 根据id查找房屋信息：
        elif choose == 2:
            find_house()
        # 修改房屋信息
        elif choose == 4:
            change_house()
main()
