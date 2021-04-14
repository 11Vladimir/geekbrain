#!/usr/bin/env python3


value_input = [input('Введите через пробел переменные для перемножения: ')]


def multiplication_table(value):
    """'Функция вывода таблицы умножения AxB'"""
    value = str(value[0]).split()
    for el in range(1, int(value[0]) + 1):
        for el_2 in range(1, int(value[1]) + 1):
            print(f'{el} * {el_2} = ', el * el_2)


multiplication_table(value_input)