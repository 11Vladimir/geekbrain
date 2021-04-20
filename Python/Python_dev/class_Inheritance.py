#!/usr/bin/env python3


class ItemDiscount:
    """
    Create price product
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def create_price_product(self):
        price = {self.product: self.price}
        return price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return super().create_price_product()


price = ItemDiscountReport('Toyta', 1000)
print(price.get_parent_data())