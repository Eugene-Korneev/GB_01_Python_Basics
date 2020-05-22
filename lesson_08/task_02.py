# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    pass


class MyInt(int):
    def __init__(self, value):
        super(MyInt, self).__init__()
        self._value = value

    def __truediv__(self, other):
        if other == 0:
            raise MyZeroDivisionError
        return self._value / other


user_input = [10, 100, 0, -5, -10]
dividend = MyInt(100)

for num in user_input:
    print(f"Делю {dividend} на {num}")
    try:
        print(f"Результат: {dividend / num}")
    except MyZeroDivisionError:
        print(f"Ошибка: на ноль делить нельзя")
