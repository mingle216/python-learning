# @Version  : 1.0
# @Author   : mmh
# @File     : 07_nested_if_example.py
# @Time     : 2024/10/16 13:25


score = float(input("请输入你的比赛成绩："))
if 0 <= score <= 10:
    gender = input("请输入你的性别：")
    if gender == "女":
        if score > 8.0:
            print(score, gender, "🎉进入决赛")
        else:
            print(score, gender, "淘汰")
    elif gender == "男":
        if score > 8.0:
            print(score, gender, "🎉进入决赛")
        else:
            print(score, gender, "淘汰")
else:
    print(score, "成绩输入错误，请重新输入！")


month = int(input("请输入月份："))
if 1 <= month <= 12:
    age = int(input("请输入年龄："))
    if 4 <= month <= 10:
        if 18 <= age <= 60:
            print("成人请付款---60元")
        elif 1 <= age < 18:
            print("儿童半价，请付款---30元")
        elif age > 60:
            print("老人三分之一，请付款---20元")
    else:
        if 18 <= age <= 60:
            print("成人请付款---40元")
        else:
            print("其他，请付款---20元")
else:
    print("月份输入错误！")