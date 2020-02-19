"""
Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from collections import defaultdict


class Warehouse:
    _d = defaultdict(dict)

    def __init__(self, department, t, count=0):
        self.department = department
        self.t = t
        self.count = count
        self._check(department, t, count)

    @classmethod
    def _ad(cls, department, t, count):
        if t not in cls._d[department]:
            cls._d[department][t] = count
        else:
            cls._d[department][t] += count

    def _check(self, department, t, count):
        if type(count) == int:
            Warehouse._ad(department, t, count)
        else:
            print("Должно быть целоечисло")
            self.department = None
            self.count = None
            self.t = None

    @property
    def get_all(self):
        return Warehouse._d

    def __del__(self):
        Warehouse._d[self.department][self.t] -= self.count


class Ofec:
    def __init__(self, t, power="on"):
        self.t = t
        self.power = power

    def __call__(self):
        return self.t


class Printer(Ofec):
    def __init__(self, catridge=100, t="printer", power="on"):
        super().__init__(t, power)
        self.catridge = catridge


class Scanner(Ofec):
    def __init__(self, mark_of_lamp, t="scan", power="on"):
        super().__init__(t, power)
        self.mark_of_lamp = mark_of_lamp


class Xerox(Ofec):
    def __init__(self, mark_of_lamp, catridge=100, t="xerox", power="on"):
        super().__init__(t, power)
        self.mark_of_lamp = mark_of_lamp
        self.catridge = catridge


p1 = Printer(catridge=20)
s1 = Scanner("Nibm")
x1 = Xerox("Zda")
w1 = Warehouse("b", p1(), 7)
w2 = Warehouse("b", s1(), 5)
w3 = Warehouse("b", p1(), 3)
w4 = Warehouse("c", x1(), 5)
print(w4.get_all)
del(w2)
print(w4.get_all)