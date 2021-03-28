#!/usr/bin/env python3


import requests
from datetime import datetime
from decimal import getcontext
from decimal import Decimal


CURRENCIES = {}
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
TEST = ['USD', 'EUR', 'AAA']

response = requests.get(url)
for id in response.text.split('<CharCode>')[1:]:
    char_code = id.split('</CharCode>')[0]
    nominal = int(id.split('<Nominal>')[1].split('</Nominal>')[0])
    name_currency = id.split('<Name>')[1].split('</Name>')[0]
    value_currency = float(id.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
    correct_value = round(value_currency / nominal, 2)
    CURRENCIES[char_code.lower()] = name_currency, correct_value


def currency_rates(currency):
    return CURRENCIES.get(currency.lower())


for char in TEST:
    print(currency_rates(char))

print('*' * 100)
"""
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. 
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""


getcontext().prec = 3  
for id in response.text.split('<CharCode>')[1:]:
    char_code = id.split('</CharCode>')[0]
    nominal = int(id.split('<Nominal>')[1].split('</Nominal>')[0])
    name_currency = id.split('<Name>')[1].split('</Name>')[0]
    value_currency = float(id.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
    correct_value = round(value_currency / nominal, 2)
    CURRENCIES[char_code.lower()] = name_currency, correct_value

    DATE = datetime.strptime(response.text.split('" name="')[0].split('<ValCurs Date="')[-1], "%d.%m.%Y").strftime('%d.%m.%Y')


def currency_rates(currency):
    if currency and CURRENCIES.get(currency.lower()):
        return CURRENCIES.get(currency.lower()), DATE


for test in TEST:
    print(currency_rates(test))