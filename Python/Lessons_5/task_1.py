#!/usr/bin/env python3

"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""

def odd_generation(number):
    """
    Generation odd number.

    Return list odd number whith operator yeld.
    """
    for id in range(number + 1):
        if id % 2 != 0:
            yield id


number = int(input('Введите число для формирования списка: '))

odd_list = odd_generation(number)

for idx in odd_list:
    print(idx, end=' ')

