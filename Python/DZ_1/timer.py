#!/usr/bin/env python3

"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d.* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений 
продолжительности, будет ли тут полезен список?
"""


duration= int(input('Введите значение продолжительности в секундах: '))


if duration // 86400 != 0:
    days = int(duration / 3600 / 24)
    duration -= int(days * 86400)
    hour = duration // 3600
    minutes = duration % 3600 / 60
    second = duration % 3600 % 60
    print(f'{int(days)} дн {int(hour)} час {int(minutes)} мин {int(second)} сек')
elif duration // 3600 != 0:
    hour = duration / 3600
    minutes = duration % 3600 / 60
    second = duration % 3600 % 60
    print(f'{int(hour)} час {int(minutes)} мин {int(second)} сек')
elif duration // 60 != 0:
    hour = duration / 3600
    minutes = duration % 3600 / 60
    second = duration % 3600 % 60
    print(f'{int(minutes)} мин {int(second)} сек')
else:
    print(f'{duration} сек')
