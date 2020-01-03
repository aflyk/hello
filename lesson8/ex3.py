def attack(avatar, target):
    target['health'] = target['health'] - atk(avatar['damage'], target["armor"])

def atk(damage, armor):
    return damage/armor


player = {
    "name" : input("Введите имя вашего персонажа: "),
    "health" : 100,
    "damage" : 12,
    "armor" : 1.2
         }
enemy = {
    "name" : "Злой гоблин",
    "health" : 50,
    "damage" : 24,
    "armor" : 1.2
        }

print(f"{player['name'].title()} нападает на {enemy['name']}")
print("Характеристики игрока")
print(player)
print("Характеристики цели")
print(enemy)
attack(player, enemy)
print(enemy)
