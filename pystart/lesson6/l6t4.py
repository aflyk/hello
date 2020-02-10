"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""
import time


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        self.speed += 10
        return f"Мы едем по трассе со скоростью {self.speed}"

    def stop(self):
        print("Начинаем торможение")
        while self.speed > 0:
            self.speed -= 20
            time.sleep(1)
        self.speed = 0
        return "Остановка завершена."

    def turn(self, direction):
        return f"Тачила {self.name} повернула {direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


class SportCar(Car):
    def go(self):
        self.speed += 30
        return f"Мы мчим по трассе со скоростью {self.speed}"

    def stop(self):
        print("Начинаем торможение")
        while self.speed > 0:
            self.speed -= 20
        self.speed = 0
        return "Остановка завершена."

# хорошая мысля приходит опосля, можно быоло сделать вызов принтов через функцию, но уже сделано и так)
car1 = PoliceCar(90, "white", "tachila 2019")
print(car1.color)
print(car1.name)
print(car1.speed)
print(car1.go())
print(car1.turn("right"))
print(car1.stop())
print(car1.speed)
print(car1.show_speed())
print("*"*50)
car2 = WorkCar(30, "black", "Podnimator")
car3 = TownCar(50, "yellow", "Жигули")
car4 = SportCar(90, "red", "ВедерКо")
print(car2.color)
print(car2.name)
print(car2.speed)
print(car2.go())
print(car2.turn("right"))
print(car2.stop())
print(car2.speed)
print(car2.show_speed())
print("*"*50)
print(car3.color)
print(car3.name)
print(car3.speed)
print(car3.go())
print(car3.turn("right"))
print(car3.stop())
print(car3.speed)
print(car3.show_speed())
print("*"*50)
print(car4.color)
print(car4.name)
print(car4.speed)
print(car4.go())
print(car4.turn("right"))
print(car4.stop())
print(car4.speed)
print(car4.show_speed())
