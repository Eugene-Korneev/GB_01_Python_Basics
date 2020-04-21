# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# number = int(input("Введите целое положительное число: "))
number = int("1357642")
result = 0

while True:
    quotient = number // 10
    remainder = number % 10

    if result < remainder:
        result = remainder

    if quotient == 0:
        break

    number = quotient

print(f"Самая большая цифра в введённом числе: {result}")
