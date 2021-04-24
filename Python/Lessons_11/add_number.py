#!/usr/bin/env python3


class NotNumber(Exception):
    def __init__(self, message):
        self.message = message


    @staticmethod
    def cheak_number(number):
        try:
            return True if int(number) else False
        except ValueError:
            return False


def add_number_list():
    resault_list = []
    while True:
        number = input('Введите число или "stop" для выхода: ')
        if number == 'stop':
            break
        try:
            if NotNumber.cheak_number(number):
                resault_list.append(int(number))
            else:
                raise NotNumber('Not number! Try again...')
        except NotNumber as message:
            print(message)
            continue
    print(resault_list)

if __name__ == '__main__':
    add_number_list()
