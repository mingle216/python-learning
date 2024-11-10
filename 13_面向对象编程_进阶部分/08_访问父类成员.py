# @Version  : 1.0
# @Author   : mmh
# @File     : 08_访问父类成员.py
# @Time     : 2024/11/9 15:07
class A:
    n1 = 100

    def run(self):
        print("A-run().....")


class B(A):
    n1 = 200

    def run(self):
        print("B-run().....")

    def say(self):
        print(f"父亲的n1 {A.n1} 本类的n1 {self.n1}")
        # 调用父类的run
        A.run(self)
        # super().run()
        # 调用本类的run
        self.run()

    def hi(self):
        print(f"父类的n1 {self.n1}")
        # 调用父类的run
        super().run()


b = B()
b.say()
# print("------------")
# b.hi()
