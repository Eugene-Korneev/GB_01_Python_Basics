# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина '{self.name}' поехала")

    def stop(self):
        print(f"Машина '{self.name}' остановилась")

    def turn(self, side):
        if side == 'l':
            side = 'налево'
        elif side == 'r':
            side = 'направо'
        else:
            print("Ошибка. Неверно указано направление.\n"
                  "Введите 'l' - для поворота налево, 'r' - направо)")
            return
        print(f"Машина '{self.name}' повернула {side}")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Вы превысили скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Вы превысили скорость!")


class PoliceCar(Car):
    pass


def show_car_info(car):
    print(f"Имя: {car.name}")
    print(f"Цвет: {car.color}")
    print(f"Полиция?: {'да' if car.is_police else 'нет'}")
    car.show_speed()
    print()


town_car = TownCar(70, 'чёрный', 'городское авто')
sport_car = SportCar(100, 'красный', 'спортивное авто')
work_car = WorkCar(20, 'жёлтый', 'дорожный каток')
police_car = PoliceCar(100, 'синий', 'патрульное авто', True)

town_car.go()
town_car.stop()
police_car.go()
police_car.turn('r')
police_car.turn('l')
police_car.stop()

cars = (town_car, sport_car, work_car, police_car)
for c in cars:
    show_car_info(c)
