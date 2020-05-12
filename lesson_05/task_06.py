# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import os
from collections import defaultdict

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_06.txt')

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_lines = f.readlines()

subject_activities = defaultdict(int)
for line in file_lines:
    for act in line.split()[1:]:
        if act == '-':
            continue
        act_num = int(''.join(filter(str.isdigit, act)))
        subject = line.split()[0].rstrip(':')
        subject_activities[subject] += act_num

print(dict(subject_activities))
