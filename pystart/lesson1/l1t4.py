"""
Пользователь вводит целое положительное число. Найдите самую
большую цифру в числе. Для решения используйте цикл while и
арифметические операции.
"""
# можно сделать 1 строчкой
# print(max(list(map(int,input()))))

user_input = int(input("Введите число:\n>>>"))
max_digit = float("-inf")

while user_input > 0:
    digit = user_input % 10
    if digit > max_digit:
        max_digit = digit
    user_input //= 10

print(max_digit)
