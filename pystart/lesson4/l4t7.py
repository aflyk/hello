"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом:
for el in fibo_gen(). Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

# не очень понял, но вроде так

def fibo_gen():
    rez = 1
    for i in range(1, 16):
        rez *= i
        yield rez


print([i for i in fibo_gen()])