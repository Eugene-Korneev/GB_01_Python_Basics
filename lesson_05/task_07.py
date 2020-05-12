# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json
import os

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_07.txt')
JSON_FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_07.json')

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_lines = f.readlines()

firm_profit_loss = []
profit_list = []
for line in file_lines:
    firm, _, income, loss = line.split()
    profit = int(income) - int(loss)
    firm_profit_loss.append({firm: profit})
    if profit >= 0:
        profit_list.append(profit)

average_profit = round(sum(profit_list) / len(profit_list))
firm_profit_loss.append({"average_profit": average_profit})
print("Получены данные о прибыли:")
print(firm_profit_loss)

print("Сохраняю данные в JSON...")
with open(JSON_FILE_PATH, 'w', encoding='utf-8') as f:
    json.dump(firm_profit_loss, f, indent=2)
print("Данные успешно сохранены")
