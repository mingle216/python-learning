# @Version  : 1.0
# @Author   : mmh
# @File     : 01_feed_cat_oop.py
# @Time     : 2024/11/7 14:34

# 定义一个猫类。 age,name,color 是属性，或者成为成员变量
# cat类 就是你自己定义的一个新类型

# 定义cat类
class Cat:
    # age,name,color是属性
    age = None
    name = None
    color = None


# 通过cat 类，创建 实例（实例对象/对象）
cat1 = Cat()

# 通过对象名.属性名 可以给各个属性赋值
cat1.name = "小白"
cat1.age = 2
cat1.color = '白色'

# 通过对象名.属性名，可以访问到属性
print(f"cat1的信息为：name:{cat1.name}, age:{cat1.age}, color:{cat1.color}")



