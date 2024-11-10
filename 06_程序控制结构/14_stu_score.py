# @Version  : 1.0
# @Author   : mmh
# @File     : 14_stu_score.py
# @Time     : 2024/10/31 20:08
# 1.统计3个班上成绩情况，每个班有5名同学，要求完成
# 2.求出各个班上的平均分和所有班级的平均分，学生的成绩从键盘键入
# 3.统计三个班及格人数

# 班级平均分
p_ban = 0
# 年级平均分
p_nan = 0
# 三个班及格人数
num = 0
# 所有班级的成绩
all_score = 0
# 所有班级的平均分
p_score = 0
for i in range(1, 4):
    t = 0
    # 每个班级的总分
    ban_score = 0
    for j in range(5):
        t = float(input(f"请输入{i}班成绩:"))
        # 每个班的成绩
        ban_score += t
        # 所有班级的成绩
        all_score += t
        if t >= 60:
            num += 1
    print(f"{i}班平均分为：", float(ban_score/5))
print("3个班总合格人数为：",num)
print("所有班级的平均分为：",float(all_score/15))