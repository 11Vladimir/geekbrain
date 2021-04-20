#!/usr/bin/env python3


class ItemDiscount:
    """
    Create price product
    """

    def __init__(self, product, price):
        self.__product = product
        self.__price = price


    def create_price_product(self):
        price = {self.__product: self.__price}
        return price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, product, price, discount):
        super().__init__(product, price)
        self.discount = discount
    

    def __int__(self):
        self.discount = discount


    def __str__(self):
        return str(self._ItemDiscount__price * (100 - self.discount)/100)


car = ItemDiscount('mazda', 1000)
discount_price = ItemDiscountReport('mazda', 1000, 10)
print(discount_price)
