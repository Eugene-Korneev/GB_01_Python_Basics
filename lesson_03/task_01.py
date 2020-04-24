# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(number_1, number_2):
    if number_2 == 0:
        return None
    return number_1 / number_2


# num_1 = input("Введите первое число: ")
num_1 = '5'
# num_2 = input("Введите второе число: ")
num_2 = '2'
num_1, num_2 = float(num_1), float(num_2)

result = divide(num_1, num_2)
if result is None:
    print("Ошибка! Деление на 0")
else:
    print(f"Результат деления: {f'{result:.2f}'.rstrip('0').rstrip('.')}")
