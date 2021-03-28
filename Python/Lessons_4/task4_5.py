import requests
from datetime import datetime
from decimal import getcontext
from decimal import Decimal
from sys import argv


CURRENCIES = {}
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
TEST = ['USD', 'EUR', 'AAA']


response = requests.get(url)
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


if __name__ == '__main__':
    if len(argv) > 1:
        for curr in argv[1:]:
            print(currency_rates(curr))