#!/usr/bin/env python3


class Date:
    def __init__(self, day, mouth, year):
        self.day = day
        self.mouth = mouth
        self.year = year


    @classmethod
    def date_from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date1 = cls(day, month, year)
        return date1


    @staticmethod
    def is_date_valid(date_string):
        day, month, year = map(int, date_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


    def __str__(self):
        return f'{self.day}, {self.mouth}, {self.year}'


date = Date.date_from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print(date)
print(is_date)
