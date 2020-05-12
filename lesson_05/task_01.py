# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os

CURRENT_DIR = os.path.curdir
user_input_lines = []

# для имитации пользовательского ввода
user_input_imitation = ['Строка 1', 'Строка 2', '333', '']
i = 0

while True:
    # user_input = input("Введите строку или 'Enter' - для завершения: ")

    # имитация пользовательского ввода
    user_input = user_input_imitation[i]
    i += 1

    if not user_input:
        break
    user_input_lines.append(f"{user_input}\n")

file_path = os.path.join(CURRENT_DIR, 'files', 'task_01.txt')
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(user_input_lines)
