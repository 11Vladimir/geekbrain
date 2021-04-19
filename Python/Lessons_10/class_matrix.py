#!/usr/bin/env python3


class Matrix:
    def __init__(self, lists):
        self.lists = lists
    

    def __str__(self):
        return '\n'.join('\t'.join([str(el) for el in line]) for line in self.lists)
    

    def __add__(self, other):
        return Matrix([map(sum, zip(*el)) for el in zip(self.lists, other.lists)])



rows = int(input("Введите количество строк и столбцов матрицы: "))
cols = rows

matrix1 = Matrix([[el * line for line in range(rows)] for el in range(cols)])
matrix2 = Matrix([[el + line for line in range(rows)] for el in range(cols)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Summ of first and second matrix:\n', matrix1 + matrix2)