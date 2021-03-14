#!/usr/bin/env python3


"""
Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». 
Вывести все склонения для проверки.
"""

userNumber = int(input('Введите число до 20 для склонения: '))

if userNumber == 1:
    print(f'{userNumber} процент')
elif 1 < userNumber < 5:
    print(f'{userNumber} процента')
else:
    print(f'{userNumber} процентов')