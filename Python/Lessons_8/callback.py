#!/usr/bin/env python3
from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            for el in args:
                if not callback(el):
                    raise ValueError('Wrong val', el)
            return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(6)
print(a)

a = calc_cube(0)
print(a)
