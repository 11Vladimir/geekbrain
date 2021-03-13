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

