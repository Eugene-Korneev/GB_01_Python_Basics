# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, values):
        self._values = values
        self._size = (len(values), len(values[0]))

    def get_size(self):
        return self._size

    def get_values(self):
        return self._values

    def __str__(self):
        max_value_len = self._get_max_value_len()
        str_rows = [f"{' '.join(map(lambda x: f'{x:>{max_value_len}}', row))}\n" for row in self._values]
        return ''.join(str_rows)

    def _get_max_value_len(self):
        max_len = 3
        for row in self._values:
            row_max_len = max(map(lambda x: len(str(x)), row))
            if row_max_len > max_len:
                max_len = row_max_len
        return max_len

    def __add__(self, other):
        other_size = other.get_size()
        other_values = other.get_values()
        if self.get_size() != other.get_size():
            raise ValueError("Error! Addition operation is not possible for different sized matrices")

        result_values = []
        for row_idx in range(self._size[0]):
            row_values = [self._values[row_idx][col_idx] + other_values[row_idx][col_idx]
                          for col_idx in range(self._size[1])]
            result_values.append(row_values)
        return Matrix(result_values)


matrix_1 = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8],
])

matrix_2 = Matrix([
    [8, -15, 4],
    [6, 22, 18],
    [28, -35, 16],
])

matrix_3 = matrix_1 + matrix_2

print(f"Матрица_1:\n{matrix_1}")
print(f"Матрица_2:\n{matrix_2}")
print(f"Матрица_1 + Матрица_2:\n{matrix_3}")
