"""
Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    rez = 1

    if x == 0:
        return 0

    for _ in range(y, 0):
        rez *= x

    return 1/rez


def my_func1(x, y):

    rez = 1
    sx = str(x)
    sign_frac = len(sx) - sx.find(".") - 1
    x = int(sx.replace('.', ''))

    if x == 0:
        return rez

    crutch = sign_frac
    sign_frac = 0

    for _ in range(y, 0):
        d = rez
        for i in range(x-1):
            rez += d
        sign_frac += crutch

    sx = str(rez)
    rez = float((sx[:-sign_frac] + '.' + sx[-sign_frac:]))
    print(rez)
    return 1/rez


while True:
    try:
        x = float(input("Введите действительное положительное число "))
        y = int(input("Ввеите отрицательное целое число "))
        if x < 0 or y > 0:
            print("некорректный ввод")
        else:
            print(my_func(x, y))
            print(my_func1(x, y))
    except ValueError:
        print("x >= 0,(х принимает действительные положительные числа)\n\
y <= 0 (y принимает только целые значения)")
