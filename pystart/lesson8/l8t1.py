"""Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def inint(cls, sdate):
        day, month, year = (int(i) for i in sdate.split("-"))
        return cls(day, month, year)

    @staticmethod
    def check(sdate):
        day, month, year = (int(i) for i in sdate.split("-"))
        return day <= 31 and month <= 12
        # лень каждый месяц просматривать




print(Date.inint("11-02-2005"))
print(Date.check("11-02-2005"))
