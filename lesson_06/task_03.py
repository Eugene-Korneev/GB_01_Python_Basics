# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum(self._wage.values())


worker1 = Position('Иван', 'Иванов', 'Продавец', 20000, 5000)
print(f"Работник: {worker1.get_full_name()}")
print(f"Общий доход: {worker1.get_total_income()}")

worker2 = Position('Пётр', 'Петров', 'Менеджер', 15000, 20000)
print(f"Работник: {worker2.get_full_name()}")
print(f"Общий доход: {worker2.get_total_income()}")
