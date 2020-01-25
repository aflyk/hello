def name_change(name, age, city):	
    return(f"{name.title()}, {age} год(а), проживает в городе {city.title()}")



name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")
print(name_change(name, age, city))
