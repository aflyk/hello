"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("pen")

    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("pencil")

    def draw(self):
        print("Карандашик трудится")


class Handle(Stationery):
    def __init__(self):
        super().__init__("handle")

    def draw(self):
        print("Выделяем макркером")


def fpr(*l):
    for i in l:
        print(f"щас работаем {type(i)}")
        i.draw()


ob1 = Stationery("кисть")
ob2 = Handle()
ob3 = Pen()
ob4 = Pencil()
fpr(ob1, ob2, ob3, ob4)
