name = input("Введите имя и фамилию: ")
age = int(input("Введите возраст: "))
weight = int(input("Введите вес: "))
status = None

if age < 30 and 50 <= weight <= 120: status = "хорошее состояние"
elif age > 40 and (weight < 50 or weight > 120): status = "следует заняться собой"
elif age > 30 and (weight < 50 or weight > 120): status = "следует обратиться к врачу!"
else: status = "не переживайте, бывает всякое"

print(f"{name}, {age} год, вес {weight} - {status}")