n = int(input("Введите число от 1 до 9: "))

while n <= 0 or n >= 10:
    n = int(input("Введите число от 1 до 9: "))

print(n**2)