# @Version  : 1.0
# @Author   : mmh
# @File     : 25_set_exercise.py
# @Time     : 2024/11/5 13:00
from readline import add_history

s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '二狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}

s_student = s_history | s_english | s_politic
print(f"选课学生一共有:{len(s_student)}个人")

print(f"只选了第一个学科的学生数量为：{len(s_history)},选了第一个学科的学生为：{s_history - s_politic - s_english}")

s1 = s_history - s_politic - s_english
s2 = s_politic - s_history - s_english
s3 = s_english - s_politic - s_history
s_one = s1| s2 | s3
print(f"只选择一门学科的学生数量为：{len(s_one)},学生名字为：{s_one}")

print(f"选择三门学科的学生数量为：{len(s_history & s_politic & s_english)},学生名字为：{s_history & s_politic & s_english}")