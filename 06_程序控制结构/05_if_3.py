# @Version  : 1.0
# @Author   : mmh
# @File     : 05_if_3.py
# @Time     : 2024/10/16 12:59

score = int(input("请输入小头儿子的考试成绩："))
if 0 <= score <= 100:
    if score == 100:
        print("奖励一辆BMW")
    elif score > 80:
        print("奖励一台iphone16")
    elif score >= 60:
        print("奖励一个ipad")
    else:
        print("🎉奖励一个大嘴巴子")
else:
    print(f"{score}输入不正确，重新输入！")
