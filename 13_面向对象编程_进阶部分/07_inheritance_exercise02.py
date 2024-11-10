# @Version  : 1.0
# @Author   : mmh
# @File     : 07_inheritance_exercise02.py
# @Time     : 2024/11/9 14:41

class Computer:
    cpu = None
    nv = None
    yp = None

    def __init__(self, cpu, nv, yp):
        self.cpu = cpu
        self.nv = nv
        self.yp = yp


    def get_details(self):
        return f"cpu: {self.cpu}, 内存: {self.nv}, 硬盘: {self.yp}"


class PC(Computer):
    brand = None

    def __init__(self, brand, cpu, nv, yp):
        self.brand = brand
        # 通过super().__init__(cpu,nv,yp)来完成对父类属性的初始化任务
        super().__init__(cpu,nv,yp)
        # self.cpu = cpu
        # self.nv = nv
        # self.yp = yp

    def get_info(self):
        return f"品牌：{self.brand} "+self.get_details()

class NotePad(Computer):
    color = None

    def __init__(self, color, cpu, nv, yp):
        self.color = color
        # 通过super().__init__(cpu,nv,yp)来完成对父类属性的初始化任务
        super().__init__(cpu,nv,yp)
        # self.cpu = cpu
        # self.nv = nv
        # self.yp = yp

    def get_info(self):
        return f"颜色：{self.color} "+self.get_details()

pc = PC("联想","amd",16,1024)
notepad = NotePad("深灰色","amd",16,1024)
print(pc.get_info())
print(notepad.get_info())