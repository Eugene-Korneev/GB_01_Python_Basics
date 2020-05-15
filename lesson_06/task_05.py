# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} пишет текст\n")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} рисует эскиз\n")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"{self.title} выделяет текст\n")


pen = Pen('Синяя ручка')
pen.draw()
pencil = Pencil('Простой карандаш')
pencil.draw()
handle = Handle('Жёлтый маркер')
handle.draw()
