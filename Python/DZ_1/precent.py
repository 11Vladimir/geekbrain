#!/usr/bin/env python3


"""
Реализовать склонение слова «процент» для чисел до 20. 
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». 
Вывести все склонения для проверки.
"""

userNumber = int(input('Введите число до 20 для склонения: '))

for i in range(1, userNumber + 1):
    if i == 1:
        print(f'{i} процент')
    elif 1 < i < 5:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
