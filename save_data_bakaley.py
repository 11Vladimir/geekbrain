#!/usr/bin/env python3
import sys


sales = sys.argv[1:]

if len(sales) >= 1:
    with open('sales_bakaley.csv', 'a', encoding='utf-8') as sale_bak:
        for price in sales:
            sale_bak.write(f'{price}\n')
