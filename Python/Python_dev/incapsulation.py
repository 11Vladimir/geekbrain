#!/usr/bin/env python3


class ItemDiscount:
    """
    Create price product
    """
    def __init__(self, product, price):
        self.__product = product
        self.__price = price

    def __create_price_product(self):
        price = {self.__product: self.__price}
        return price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return super()._ItemDiscount__create_price_product()


price = ItemDiscountReport('Toyta', 1000)
print(price.get_parent_data())