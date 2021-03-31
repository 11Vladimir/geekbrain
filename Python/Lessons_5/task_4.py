#!/usr/bin/env python3


"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
"""


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1]]

print('Список чисел значение которых больше придыдущих: ', result)


