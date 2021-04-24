#!/usr/bin/env python3


class MyError(Exception):
    """Class for exceptions in this module."""
    def __init__(self, text):
        super().__init__()
        self.text = text
    
    def __str__(self):
        return repr(self.text)



def division_number(*args):
    """Division two numbers. And cheak zero number"""
    
    while True:
        if 'stop' in args: 
            break
        try:
            if float(args[1]) == 0:
                raise MyError('You cannot divide by zero!')
            else:
                print(f'{float(args[0]) / float(args[1]):.2f}')
                break
        except MyError as message:
            print(message)
            break
        except ValueError as message:
            print(message)


division_number(5, 2)
