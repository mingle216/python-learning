# @Version  : 1.0
# @Author   : mmh
# @File     : 04_recursion01.py
# @Time     : 2024/11/1 14:28

# def test(n):
#     if n > 2:
#         test(n - 1)
#     else:
#         print("n=", n)
#
#
# test(4)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))