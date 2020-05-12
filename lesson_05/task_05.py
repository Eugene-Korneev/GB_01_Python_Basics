# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os
from random import randint

FILE_PATH = os.path.join(os.path.curdir, 'files', 'task_05.txt')

# write numbers to file
numbers = ' '.join([str(randint(0, 100)) for _ in range(randint(10, 20))])
with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write(numbers)

# read numbers from file and calculate sum
with open(FILE_PATH, 'r', encoding='utf-8') as f:
    file_str = f.read()
file_numbers = file_str.strip().split()
file_numbers = [int(n) for n in file_numbers]
print(f"Сумма чисел в файле: {sum(file_numbers)}")
