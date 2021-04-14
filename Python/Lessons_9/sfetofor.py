#!/usr/bin/env python3


import time


class Sfetofor:
    def __init__(self):
        self.__color = {
            'Red': 7, 
            'Yeollow': 2, 
            'Green': 2
            }
 

    def __change_color(self):
        for color, sec in self.__color.items():
            if color == 'Red':
                print(color)
                for i in range(sec, 0, -1):
                    print(f"{i}", end="\r", flush=True)
                    time.sleep(1)
            elif color == 'Yeollow':
                print(color)
                for i in range(sec, 0, -1):
                    print(f"{i}", end="\r", flush=True)
                    time.sleep(1)
            else:
                print(color)
                for i in range(sec, 0, -1):
                    print(f"{i}", end="\r", flush=True)
                    time.sleep(1)
    

color = Sfetofor()
color._Sfetofor__change_color()
