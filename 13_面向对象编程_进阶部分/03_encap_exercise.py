# @Version  : 1.0
# @Author   : mmh
# @File     : 03_encap_exercise.py
# @Time     : 2024/11/9 12:04
class Account:
    __name = None
    __balance = None
    __pwd = None

    # 设置默认值
    def __init__(self, name, balance, password):
        self.__name = name
        self.__balance = balance
        self.__pwd = password

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.__name = name
        else:
            print("姓名不符合要求")

    def set_balance(self, balance):
        if balance > 20:
            self.__balance = balance
        else:
            print("余额不符合要求")

    def set_password(self, password):
        if len(password) == 6:
            self.__pwd = password
        else:
            print("密码不符合要求")

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_pwd(self):
        return self.__pwd

    def query_info(self,name,password):
        if self.__name == name and self.__pwd == password:
            print("账号密码成功！！账号信息为：")
            return (f"姓名为：{self.get_name()}\n"
                    f"密码为：{self.get_pwd()}\n"
                    f"余额为：{self.get_balance()}")
        else:
            return  "姓名或密码错误，请重新输入信息！"


# 给默认值
account = Account("ming",1000,"123456")

account.set_name("tom")
account.set_password("666666")
account.set_balance(100)
print(account.query_info("tom","666666"))
