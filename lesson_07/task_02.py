# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    @abstractmethod
    def clothes_type(self):
        pass

    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(AbstractClothes):
    clothes_type = 'Пальто'

    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def calc_fabric_consumption(self):
        return self._size / 6.5 + 0.5


class Suit(AbstractClothes):
    clothes_type = 'Костюм'

    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    def calc_fabric_consumption(self):
        return 2 * self._height + 0.3


class AllClothes:
    def __init__(self):
        self._clothes = []

    def add(self, item):
        assert isinstance(item, AbstractClothes), "Error! Wrong type of data to add"
        self._clothes.append(item)

    def calc_total_consumption(self):
        return sum(c.calc_fabric_consumption() for c in self._clothes)


light_coat = Coat("Лёгкое осеннее пальто", 30)
print(f"Название: {light_coat.name}, тип: {light_coat.clothes_type},\n"
      f"Ткани затрачено на производство: {light_coat.calc_fabric_consumption():.2f} м.\n")

winter_coat = Coat("Тёплое зимнее пальто", 30)
print(f"Название: {winter_coat.name}, тип: {winter_coat.clothes_type},\n"
      f"Ткани затрачено на производство: {winter_coat.calc_fabric_consumption():.2f} м.\n")

business_suit = Suit("Деловой костюм", 1.90)
print(f"Название: {business_suit.name}, тип: {business_suit.clothes_type},\n"
      f"Ткани затрачено на производство: {business_suit.calc_fabric_consumption():.2f} м.\n")

all_clothes = AllClothes()
all_clothes.add(light_coat)
all_clothes.add(winter_coat)
all_clothes.add(business_suit)
print(f"Ткани затрачено на производство всей одежды: {all_clothes.calc_total_consumption():.2f} м.")
