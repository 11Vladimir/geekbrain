#!/usr/bin/env python3


class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass_asfalt_for_m2 = 25
        self._asphalt_thickness = 5
    
    def repear_road(self):
        print(f'{self._length}m * {self._width}m * {self._mass_asfalt_for_m2}cm * {self._asphalt_thickness}kg = ' 
        f'{(self._length * self._width * self._mass_asfalt_for_m2 * self._asphalt_thickness) / 1000}T')


road = Road(2, 20)
road.repear_road()
