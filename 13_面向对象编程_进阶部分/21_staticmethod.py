# @Version  : 1.0
# @Author   : mmh
# @File     : 21_staticmethod.py
# @Time     : 2024/11/10 14:51
class Monster:
    name = "悟空"
    age = 300

    def hi(self):
        print(f"hi() {self.name}-{self.age}")

    @staticmethod
    def ok():
        print("ok()")

# 不需要实例化，通过类即可调用静态方法
Monster.ok()
# 通过实例对象，也可以调用静态方法
monster = Monster()
monster.ok()
