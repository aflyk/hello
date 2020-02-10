"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""


import random


count_digit = random.randint(10, 100)

with open("l5t5_1.txt", "w", encoding="utf-8") as f:
    f.write(" ".join([str(random.randint(-50, 50)) for _ in range(count_digit)]))

with open("l5t5_1.txt", encoding="utf-8") as f:
    text = f.read()

print(sum(map(int, text.split())))