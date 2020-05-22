# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, imag=0.0):
        self._real = float(real)
        self._imag = float(imag)

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def __str__(self):
        real = f"{self._real:.2f}".rstrip('0').rstrip('.')
        imag = f"{self._imag:.2f}".rstrip('0').rstrip('.')
        return f"{real} + {imag}j"

    def __add__(self, other):
        real = self._real + other.real
        imag = self._imag + other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self._real * other.real - self._imag * other.imag
        imag = self._real * other.imag + self._imag * other.real
        return ComplexNumber(real, imag)


if __name__ == "__main__":
    complex_1 = ComplexNumber(1)
    complex_2 = ComplexNumber(2, 1)
    complex_3 = ComplexNumber(3.5, 2.5)

    print(complex_1 + complex_2 + complex_3)
    print(complex_1 * complex_2 * complex_3)
