#!/usr/bin/env python3

"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


odd_list = []


def odd_generation(number):
    """
    Generation odd number.

    Return list odd number whith operator return.
    """
    odd_list = [id for id in range(number +1) if id % 2 != 0]
    return odd_list


number = int(input('Введите число для формирования списка: '))

for idx in odd_generation(number):
    print(idx, end=' ')
