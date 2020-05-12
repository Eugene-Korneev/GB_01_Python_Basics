# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import os

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_03.txt')

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_lines = f.readlines()

low_salary = []
salary_sum = 0
for line in file_lines:
    employee, salary = line.split()
    salary_sum += int(salary)
    if int(salary) < 20000:
        low_salary.append(employee)

print(f"Сотрудники с окладом менее 20 тыс.: {', '.join(low_salary)}")
print(f"Средняя величина дохода сотрудников: {salary_sum / len(file_lines):.2f}")
