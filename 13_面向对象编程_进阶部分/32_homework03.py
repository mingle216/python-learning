# @Version  : 1.0
# @Author   : mmh
# @File     : 32_homework03.py
# @Time     : 2024/11/10 16:13
class Doctor:
    name = None
    age = None
    job = None
    gender = None
    sal = None

    def __init__(self, name, age, job,gender, sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal

    def __eq__(self, other):
        if isinstance(other, Doctor):
            return (self.name == other.name
                    and self.age == other.age
                    and self.job == other.job)
        else:
            return False

doctor1 = Doctor("tom",28,"牙医","男",8000)
doctor2 = Doctor("tom",28,"牙医","男",8000)
# doctor2 = Doctor("lihua",32,"内科","男",16000)
print(doctor1 == doctor2)