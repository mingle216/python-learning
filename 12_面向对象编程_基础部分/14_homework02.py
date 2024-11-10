# @Version  : 1.0
# @Author   : mmh
# @File     : 13_homework01.py
# @Time     : 2024/11/8 16:23

class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100
        else:
            self.price = self.price
        return self.price


book = Book("红楼梦",110)
print(book.update_price())
