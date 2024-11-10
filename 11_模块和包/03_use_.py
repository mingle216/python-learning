# @Version  : 1.0
# @Author   : mmh
# @File     : 03_use_.py
# @Time     : 2024/11/7 13:12
from math import fabs
import requests

# 导入包下的模块
import hsp_package.module01
import hsp_package.module02

# 使用导入的模块
hsp_package.module01.hi()
hsp_package.module02.ok()


print(fabs(-90.5))
