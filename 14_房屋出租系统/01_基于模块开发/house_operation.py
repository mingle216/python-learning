# @Version  : 1.0
# @Author   : mmh
# @File     : house_operation.py
# @Time     : 2024/11/12 21:12
"""
    说明：提供对房屋的各种操作
"""
from itertools import count
from my_tools import *
# 定义数据
house_data = [
    {"编号": 2, "房主": "tim", "电话": 113, "地址": "海淀", "月租": 800, "状态(未出租/已出租)": "已出租"},
    {"编号": 3, "房主": "bee", "电话": 116, "地址": "朝阳", "月租": 900, "状态(未出租/已出租)": "未出租"}
]


def main_menu():
    """
    显示主菜单，让用户选择
    :return:
    """
    print("房屋出租系统菜单：".center(65, "="))
    print("\t\t\t\t\t\t\t1 新 增 房 源")
    print("\t\t\t\t\t\t\t2 查 找 房 屋")
    print("\t\t\t\t\t\t\t3 删 除 房 屋 信 息")
    print("\t\t\t\t\t\t\t4 修 改 房 屋 信 息")
    print("\t\t\t\t\t\t\t5 房 屋 列 表")
    print("\t\t\t\t\t\t\t6 退    出")


def find_by_id(find_id):
    """
    根据输入的find_id返回对应的房屋信息
    :return:
    """
    for house in house_data:
        if str(house["编号"]) == find_id:
            return house


def exit_menu():
    """
    退出系统
    :return:
    """
    choice = read_confirm_select()
    if choice == 'Y':
        print("你退出了程序，欢迎下次使用....")
        return -1
    elif choice == 'N':
        return 1


def show_info():
    """
    显示房屋列表的功能
    :return:
    """
    data_keys = house_data[0].keys()
    print("房屋列表".center(65, "="))
    # 打印列表的头
    for i in data_keys:
        print(f"{i}", end="\t\t\t")
    print("")
    # 打印数据
    # for i in range(len(house_data)):
    #     for value in house_data[i].values():
    #         print(f"{value}\t\t\t", end="")
    #     print()
    for house in house_data:
        for value in house.values():
            print(f"{value}", end="\t\t\t")
        print("")
    print("房屋列表显示完毕".center(65, "="))
    print("")


def add_house():
    """
    添加房源
    :return:
    """
    print("添加房屋".center(65, "="))
    # 自动增加编号
    new_id = house_data[-1]["编号"] + 1  # 获取最后一条数据的编号并加一
    # 从键盘获取新条目的信息
    new_owner = input("请输入房主姓名: ")
    new_phone = input("请输入电话: ")
    new_address = input("请输入地址: ")
    new_rent = int(input("请输入租金: "))
    new_status = input("请输入状态 (未出租/已出租): ")
    # 创建新的条目
    new_entry = {
        "编号": new_id,
        "房主": new_owner,
        "电话": new_phone,
        "地址": new_address,
        "月租": new_rent,
        "状态(未出租/已出租)": new_status
    }
    house_data.append(new_entry)
    # 打印增加后的 house_data 列表
    print("\n更新后的数据列表:")
    for record in house_data:
        print(record)
    print("添加房屋成功".center(65, "="))


def delete_house():
    """
    删除房屋信息
    :return:
    """
    print("删除房屋".center(65, "="))

    # data_keys = []
    # for i in house_data:
    #     data_keys.append(i["编号"])
    while True:
        choose_num = input("请输入你要删除房屋的编号(-1退出):")
        choice=read_confirm_select()
        house=find_by_id(choose_num)
        if choose_num == -1:
            print("放弃删除房屋信息".center(65, "="))
            break
        elif house and choice == 'Y':
            house_data.remove(house)
            print("删除房屋信息成功".center(65, "="))
            break  # 找到之后立即停止循环
        elif house and choice == 'N':
            print("已退出，请重新输入".center(65, "="))
            continue
        else:
            print("房屋编号不存在，删除失败".center(65, "="))
            continue


def find_house():
    """
    查找房源信息
    :return:
    """
    print("查找房屋信息".center(65, "="))
    # data_keys = []
    # # 编号列表
    # for i in house_data:
    #     data_keys.append(str(i["编号"]))
    # print(data_keys)
    while True:
        find_num = input("请输入要查找的id(-1退出):")
        house = find_by_id(find_num)
        # 1.查找在不在data_keys编号列表中
        if find_num == '-1':
            break
        elif house:
            # 打印列表的头
            data_head = house_data[0].keys()
            for i in data_head:
                print(f"{i}\t\t\t", end="")
            print("")
            # 根据所在下标打印房屋信息
            for value in house.values():
                print(f"{value}\t\t\t", end="")
            print("")
            print("查找房屋信息成功".center(65, "="))
            continue
        elif not find_num.isdigit():
            print(f"{find_num}不是数字,请重新输入".center(65, "="))
        elif house is None:
            print(f"查找房屋信息id{find_num}不存在".center(65, "="))


def change_house():
    """
    修改房屋信息
    """
    print("修改房屋信息".center(65, "="))

    while True:
        choose_num = input("请选择你要修改房屋的编号(-1退出): ")
        house = find_by_id(choose_num)
        if choose_num == '-1':
            break
        elif house:
            # 获取修改信息，按需输入，按 Enter 跳过不修改
            new_owner = input(f"姓名({house['房主']}): ")  # 使用单引号来引用字段名
            if new_owner:
                house["房主"] = new_owner

            new_phone = input(f"电话({house['电话']}): ")
            if new_phone:
                house["电话"] = int(new_phone)  # 确保输入是整数

            new_address = input(f"地址({house['地址']}): ")
            if new_address:
                house["地址"] = new_address

            new_rent = input(f"租金({house['月租']}): ")
            if new_rent:
                house["月租"] = int(new_rent)  # 确保输入是整数
            new_status = input(f"状态({house['状态(未出租/已出租)']}): ")
            if new_status:
                house["状态"] = new_status
            continue  # 修改完毕，退出循环
        else:
            print("没有要修改的房屋信息".center(65, "="))
