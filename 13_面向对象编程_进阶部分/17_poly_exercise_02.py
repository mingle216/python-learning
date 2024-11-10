# @Version  : 1.0
# @Author   : mmh
# @File     : 17_poly_exercise_02.py
# @Time     : 2024/11/10 10:47
class Employee:
    """
        定义员工类
    """
    __name = None
    # 月工资
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary


    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_annual(self):
        """
        计算全年工资
        :return:全年工资
        """
        return self.get_salary() * 12


class Worker(Employee):
    def work(self):
        print(f"员工：{self.get_name()}正在工作...")

    def get_annual(self):
        return super().get_annual()


class Manager(Employee):
    __bonus = None

    def __init__(self, name, salary, bonus):
        self.__bonus = bonus
        super().__init__(name, salary)

    def get_bonus(self):
        return self.__bonus

    def manager(self):
        print(f"经理：{self.get_name()}正在管理...")

    def get_annual(self):
        return super().get_annual() + self.get_bonus()


def show_emp_annual(e: Employee):
    print(f"{e.get_name()}的全年工资为：{e.get_annual()}")


def working(e: Employee):
    if isinstance(e, Worker):
        e.work()
    elif isinstance(e, Manager):
        e.manager()
    else:
        print("无法判断工作状态...")


work = Worker("ming", 6000)
manager = Manager("tom", 12000, 10000)
show_emp_annual(work)
show_emp_annual(manager)
working(manager)
working(work)
