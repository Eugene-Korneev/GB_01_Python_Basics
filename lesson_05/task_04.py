# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_04_eng.txt')
NEW_FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_04_rus.txt')
RUS_MAPPING_DICT = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два',
                    'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
                    'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь',
                    'Nine': 'Девять', 'Ten': 'Десять'}


def rus_mapping(string: str) -> str:
    for eng, rus in RUS_MAPPING_DICT.items():
        string = string.replace(eng, rus)
    return string


with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_lines = f.readlines()

file_lines = map(rus_mapping, file_lines)

with open(NEW_FILE_PATH, 'w', encoding='utf-8') as f:
    f.writelines(file_lines)
