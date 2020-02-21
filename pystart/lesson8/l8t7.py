"""
 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
 реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу
 проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
 созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexDigit:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return ComplexDigit(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        return ComplexDigit(self.i * other.i - self.j * other.j, self.i * other.j + self.j * other.j)

    def __str__(self):
        return f"{self.i} + i{self.j} " if self.j > 0 else f"{self.i} - i{-self.j} "


d1 = ComplexDigit(7,-5)
d2 = ComplexDigit(3,2)
print(d1+d2)
print(d1*d2)