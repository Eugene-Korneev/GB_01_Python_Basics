# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import os

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_02.txt')

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_lines = f.readlines()

print(f"Количество строк в файле: {len(file_lines)}")
for i, line in enumerate(file_lines):
    words = line.split()
    print(f"Количество слов в строке {i+1}: {len(words)}")
