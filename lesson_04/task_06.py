# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools


def generate_numbers(start):
    return itertools.count(start)


def iterate_list(iterable):
    return itertools.cycle(iterable)


if __name__ == '__main__':
    # 10 первых значений из бесконечного итератора, начиная со 100
    counter = generate_numbers(100)
    for _ in range(10):
        print(next(counter))

    print()

    # 10 элементов из списка, повторяя с начала при достижении конца списка
    my_list = ['one', 2, 'three']
    iterator = iterate_list(my_list)
    for _ in range(10):
        print(next(iterator))
