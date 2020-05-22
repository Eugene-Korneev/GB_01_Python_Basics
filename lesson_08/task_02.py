# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    pass


user_input = [10, 100, 0, -5, -10]

for num in user_input:
    print(f"Делю 100 на {num}")
    try:
        if num == 0:
            raise MyZeroDivisionError
        result = 100 / num
    except MyZeroDivisionError:
        print(f"Ошибка: на ноль делить нельзя")
    except Exception as e:
        print(e)
    else:
        print(f"Результат: {result}")
