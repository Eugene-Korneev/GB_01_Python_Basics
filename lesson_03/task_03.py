# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    if num_1 <= num_2 and num_1 <= num_3:
        return num_2 + num_3
    if num_2 <= num_1 and num_2 <= num_3:
        return num_1 + num_3
    return num_1 + num_2


print(my_func(5, 10, 10))
