#!/usr/bin/env python3
import sys


sales = sys.argv[1:]

if len(sales) == 0:
    with open('sales_bakaley.csv', 'r', encoding='utf-8') as sale_bak:
        for sale_data in sale_bak.readlines():
            print(sale_data.strip())
