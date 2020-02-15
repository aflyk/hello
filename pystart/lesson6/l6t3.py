"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
апример, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["wage"]*self._income["bonus"]/100:.2f}'


if __name__ == "__main__":
    user1 = Position("Rex", "T-Rex", 'Dino', 1234.43, 13)
    print(user1.name)
    print(user1.surname)
    print(user1.position)
    print(user1.get_full_name())
    print(user1.get_total_income())
    user2 = Position("Иван", "Иванов", "Охрана труда", 30000, 15)
    print(user2.get_full_name())
    print(user2.get_total_income())