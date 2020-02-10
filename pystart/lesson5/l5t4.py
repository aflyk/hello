"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


DIGIT_DICT = {"One":"Один","Two":"Два", "Three":"Три", "Four":"Четыре"}

with open("l5t4_1.txt", encoding="utf-8") as f:
    with open("l5t4_2.txt", "w", encoding="utf-8") as fw:
        for line in f:
            digit_en, _, digit = line.split()
            fw.write(f"{DIGIT_DICT[digit_en]} {_} {digit}\n")