"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите
у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

first_var = "some string"
digit_var = 5
print(first_var)
print(digit_var)
user_input_str1 = input("Введите строку\n>>> ")
user_input_digit1 = input("Введите целочисленное число\n>>> ")
flag = True
if not(user_input_digit1.isdigit()):
    print("Необходимо ввести целочисленное число")
    flag = False
else:
    user_input_digit1 = int(user_input_digit1)
print(f"Ваша строка {user_input_str1}, ваше число {user_input_digit1 if flag else 'не смогли в циферки'}")
user_input_digit2 = float(input("Теперь введите вещественное число, через точку\n>>> "))
user_input_str2 = input("Введите вторую строку\n>>> ")
print(user_input_digit2, user_input_str2)