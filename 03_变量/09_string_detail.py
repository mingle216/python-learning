# @Version  : 1.0
# @Author   : mmh
# @File     : 09_string_detail.py
# @Time     : 2024/10/14 19:55

# 字符串使用注意事项

# 使用引号('或')包括起来，创建字符串

str1 = 'tom说:"hello"'
print(str1)
str2 = 'jack说："hi"'

print(f'{type(str1)},{type(str2)}')

# 通过加号可以连接字符串
print("tom" + "hello")

# 用三个单引号'''内容'''，或三个双引号"""内容"""可以使字符串内容保持原样输出(保持原有格式)
# 在输出格式复杂的内容是比较有用的，比如输出一段代码

content = '''
However, Peter found it very dull on the hillside with only sheep for company. 
So he’d look for ways to amuse himself: running up rocks, climbing trees and even chasing sheep. 
Unfortunately, he still felt bored. Then a brilliant idea crossed his mind. 
He climbed to the top of the tallest tree, shouting towards the village: “Wolf! Wolf! Wooolf! Woohoolf!”
'''
print(content)

# 字符前加‘r’，会使整个字符串不被转义
print(r"jack\mac\abc")  # jack\mac\abc

# 讲解驻留字符串的机制
str1 = "hello"
str2 = "hello"
str3 = "hello"
# id()的函数，是可以返回对象/数据的内存地址
print("str1的地址:", id(str1))
print("str2的地址:", id(str2))
print("str3的地址:", id(str3))

num1 = "abc#"
num2 = "abc#"
print(id(num1), id(num2))

num1=-125
num2=-125
print(id(num1), id(num2))