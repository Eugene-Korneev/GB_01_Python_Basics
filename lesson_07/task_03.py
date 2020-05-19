# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, cells_num: int):
        self._cells_num = cells_num

    @staticmethod
    def _check_other_type(other):
        assert isinstance(other, Cell), "Ошибка! Не могу объединить клетку с не-клеткой"

    @property
    def cells_num(self):
        return self._cells_num

    def __str__(self):
        return f"Тип объекта: Клетка, количество ячеек в клетке: {self._cells_num}"

    def __add__(self, other):
        self._check_other_type(other)
        cells = self.cells_num + other.cells_num
        return Cell(cells)

    def __sub__(self, other):
        self._check_other_type(other)
        cells = self.cells_num - other.cells_num
        if cells < 0:
            print("Ошибка! Не могу выполнить вычитание. "
                  "Количество ячеек в клетке не может быть меньше 0")
            return
        return Cell(cells)

    def __mul__(self, other):
        self._check_other_type(other)
        cells = self.cells_num * other.cells_num
        return Cell(cells)

    def __truediv__(self, other):
        self._check_other_type(other)
        cells = self.cells_num // other.cells_num
        return Cell(cells)

    def make_order(self, cells_in_row):
        num_rows, cells_in_last_row = divmod(self._cells_num, cells_in_row)
        res = [f"{'*' * cells_in_row}\n" for _ in range(num_rows)]
        return f"{''.join(res)}{'*' * cells_in_last_row}"


cell_1 = Cell(15)
print(f"Клетка 1:\n{cell_1}\n")
cell_2 = Cell(20)
print(f"Клетка 2:\n{cell_2}\n")

print("Клетка 1 + Клетка 2:")
result = cell_1 + cell_2
print(f"{result}\n")

print("Клетка 1 - Клетка 2:")
result = cell_1 - cell_2
print(f"{result}\n")

print("Клетка 2 - Клетка 1:")
result = cell_2 - cell_1
print(f"{result}\n")

print("Клетка 1 * Клетка 2:")
result = cell_1 * cell_2
print(f"{result}\n")

print("Клетка 1 // Клетка 2:")
result = cell_1 / cell_2
print(f"{result}\n")

print("Клетка 2 // Клетка 1:")
result = cell_2 / cell_1
print(f"{result}\n")

print("Организация ячеек по рядам по 10 шт:")
print(f"Клетка 1:\n{cell_1.make_order(10)}\n")
print(f"Клетка 2:\n{cell_2.make_order(10)}")
