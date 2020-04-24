# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def print_user_data(*, name, surname, birth_year,
                    birth_city, email, phone_number):
    print(f"Информация о пользователе: {name} {surname} {birth_year} "
          f"{birth_city} {email} {phone_number}")


user = {
    'surname': 'Иванов',
    'name': 'Иван',
    'birth_year': 2000,
    'birth_city': 'Москва',
    'email': 'i_ivanov@gmail.com',
    'phone_number': 89991002020,
}

print_user_data(**user)
