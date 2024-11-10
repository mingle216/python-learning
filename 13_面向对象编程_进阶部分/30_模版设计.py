# @Version  : 1.0
# @Author   : mmh
# @File     : 30_模版设计.py
# @Time     : 2024/11/10 15:55
# 使用模版设计模式
import time
from abc import abstractmethod, ABC


class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    # 统计任务执行的时间
    def cal_time(self):
        # 得到开始的时间，毫秒数
        start = time.time() * 1000
        self.job()
        # 得到结束的时间，毫秒数
        end = time.time() * 1000
        print("计算任务 执行时间(毫秒)", end - start)


class AAA(Template):
    def job(self):
        num = 0
        for i in range(80001):
            num += i

class BBB(Template):
    def job(self):
        num = 0
        for i in range(80001):
            num -= i
aaa = AAA()
bbb = BBB()
aaa.cal_time()
bbb.cal_time()