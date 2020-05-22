# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class IsNotANumberError(Exception):
    pass


user_input = [10, 30, '50', 0, 'num', -10, -100]
result = []

for num in user_input:
    print(f"Добавляю очередной элемент {num} в массив")
    try:
        if not isinstance(num, int):
            raise IsNotANumberError("Ошибка: не могу добавить в список не-число")
        result.append(num)
    except IsNotANumberError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("Элемент успешно добавлен")

print(f"Итоговый список:\n{result}")
