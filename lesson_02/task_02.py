# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# my_list = input('Введите все элементы списка с разделением через пробел: ')
my_list = "1 2 3 4 5"
my_list = my_list.split()
print(f"Ваш список: {my_list}")

last_el = len(my_list) - 1 if len(my_list) > 1 else 1

for i in range(0, last_el, 2):
    if i < len(my_list) - 1:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f"Результат: {my_list}")
