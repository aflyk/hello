day_dict = {1 : "превое", 2 : "второе", 3 : "третье", 4 : "четвертое", 5 : "пятое", 6 : "шестое", 7:"седьмое", 8:"восьмое", 9:"девятое", 10:"десятое", 11:"одиннадцатое", 12:"двенадцатое", 13:"тринадцатое",
            14:"четырнадцатое", 15:"пятнадцатое", 16:"шестнадцатое", 17:"семнадцатое", 18:"восемнадцатое", 19:"девятнадцатое", 20:"двадцатое", 21:" двадцать превое", 22:"двадцать второе", 23:"двадцать третье",
            24:"двадцать четвертое", 25:"двадцать пятое", 26:"двадцать шестое", 27:"двадцать седьмое", 28:"двадцать восьмое", 29:"двадцать девятое", 30:"тридцатое", 31:"тридцать превое"}
month_dict = {1 : "января", 2 : "февраля", 3 : "марта", 4 : "ареля", 5 : "мая", 6 : "июня", 7 : "июля", 8 : "августа",
              9 : "сентября", 10 : "октября", 11 : "ноября", 12 : "декабря"}
user_date = [int(i) for i in input().split('.')]
print(f"{day_dict[user_date[0]]} {month_dict[user_date[1]]} {user_date[2]} года")
