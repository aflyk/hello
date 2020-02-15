"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    def __init__(self, l):
        self.matrix = l

    def __str__(self):
        rez = []
        for i in self.matrix:
            for j in i:
                rez.append(f"{j:3}")
            rez.append("\n")
        return "".join(rez)

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            rez = []
            for i in range(len(self.matrix)):
                l = []
                for j in range(len(self.matrix[0])):
                    l.append(self.matrix[i][j] + other.matrix[i][j])
                rez.append(l)
            return Matrix(rez)

row = random.randint(2,10)
column = random.randint(1,10)

l1 = [[random.randint(0,10) for j in range(column)] for i in range(row)]
print(l1)
l2 = [[random.randint(0,10) for j in range(column)] for i in range(row)]
print(l2)
m1 = Matrix(l1)
m2 = Matrix(l2)
print(m1)
print(m2)
print(m1+m2)