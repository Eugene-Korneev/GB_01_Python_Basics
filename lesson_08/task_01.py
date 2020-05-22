# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_str):
        self._date_str = date_str

    def __str__(self):
        return f"Текущая дата: {self._date_str}"

    @classmethod
    def get_date_nums(cls, date_str):
        day, month, year = cls._parse_date_to_nums(date_str)
        return day, month, year

    @staticmethod
    def _parse_date_to_nums(date_str):
        day, month, year = (int(d) for d in date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date_str(date_str):
        day_month_year = date_str.split('-')

        if not len(day_month_year) == 3:
            print(f"Данные не валидны: в строке должно быть 3 числа. "
                  f"Получено: {len(day_month_year)}")
            return

        parsed_date = []
        for d in day_month_year:
            if not d.isnumeric:
                print(f"Данные не валидны: '{d}' - не число")
                return
            parsed_date.append(int(d))

        day, month, year = parsed_date
        if not 0 < day <= 31:
            print(f"Данные не валидны: дней в месяце должно быть от 1 до 31. "
                  f"Получено: {day}")
            return
        if not 0 < month <= 12:
            print(f"Данные не валидны: номер месяца должно быть от 1 до 12. "
                  f"Получено: {month}")
            return
        if year < 0:
            print(f"Данные не валидны: номер года не может быть меньше нуля. "
                  f"Получено: {year}")
            return
        print("Введённая дата валидна")


if __name__ == '__main__':
    today_str = '22-05-2020'
    today = Date(today_str)
    print(today)
    print(Date.get_date_nums('22-05-2020'))

    Date.validate_date_str('')
    Date.validate_date_str('32-10-2020')
    Date.validate_date_str(today_str)
