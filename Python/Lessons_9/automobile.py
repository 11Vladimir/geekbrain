#!/usr/bin/env python3


class Car():
    """
    Создание и имитация поведения автомобиля
    """
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
    

    def go(self):
        print(f'Автомобиль {self.name} поехал...')
    

    def stop(self):
        print(f'Автомобиль {self.name} оставновился!')
    

    def turn(self, direction):
        print(f'{self.name}: Машина повернула: {"налево" if direction.lower() == "лево" else "направо"}.')


class TownCar(Car):
    """
    Town car
    """
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля: {self.speed}.'


class WorkCar(Car):
    """
    Work car
    """
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля: {self.speed}.'


class SportCar(Car):
    """
    Sport car
    """
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля: {self.speed}.'


class PoliceCar(Car):
    """
    Police car
    """
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
   


town_car = TownCar('Toyta', 'Red', 80)
print(town_car.show_speed())