# @Version  : 1.0
# @Author   : mmh
# @File     : 18_breakZ_exercise01.py
# @Time     : 2024/10/31 21:04

# 实现登陆验证，有三次机会，如果用户名为“张无忌”，密码“888”提示登录成功，否则提示还有几次机会，请使用for+break完成

for i in range(3):
    name = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    print(name,password)
    if name == "tom" and password == "123":
        print("登陆成功～")
        break
    else:
        print(f"还剩下{2-i}次机会")