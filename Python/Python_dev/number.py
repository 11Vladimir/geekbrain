#!/usr/bin/env python3


import sys
import numbers

number = sys.argv[1]


def find_file_name(number):
    try:
        if type(int(number)) == int:
            return ('Это целое число!')
    except ValueError:
        number = number.split('.')
        if int(number[0]) == int(number[1]):
            return True
        return False


print(find_file_name(number))
