def attack(avatar, target):
    target['health'] = target['health'] - avatar['damage']




player = {
    "name" : input("Введите имя вашего персонажа: "),
    "health" : 100,
    "damage" : 12
         }
enemy = {
    "name" : "Злой гоблин",
    "health" : 50,
    "damage" : 24 
        }

print(f"{player['name'].title()} нападает на {enemy['name']}")
print("Характеристики игрока")
print(player)
print("Характеристики цели")
print(enemy)
attack(player, enemy)
print(enemy)
