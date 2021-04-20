#!/usr/bin/env python3


class Worker():
    def __init__(self, name, surname, position, **values):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {wage: income for wage, income in values.items()}


class Position(Worker):
    def __init__(self, name, surname, position, **values):
        super().__init__(name, surname, position, **values)
    

    def full_name(self):
        print(f'Full name worker: {self.name} {self.surname} Position: {self.position}')
    

    def get_total_income(self):
        print(f'Зарплата сотрудника {self.name}а {self.surname} а составляет: {self._income["wage"] + self._income["bonus"]} евро'
)


worker = Position('Petr', 'Petrov', 'Dev', wage=1000, bonus=100)
worker.full_name()
worker.get_total_income()
