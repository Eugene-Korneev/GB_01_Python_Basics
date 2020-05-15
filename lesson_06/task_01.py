# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    _traffic_light_colors = {'green': 'зелёный', 'yellow': 'жёлтый', 'red': 'красный'}

    def __init__(self):
        self.__previous_color = self.__color = 'yellow'

    def _check_color_order(self, new_color):
        condition = (
                self.__color == 'red' and new_color == 'yellow'
                or self.__color == 'green' and new_color == 'yellow'
                or self.__previous_color in ('red', 'yellow') and self.__color == 'yellow' and new_color == 'green'
                or self.__previous_color in ('green', 'yellow') and self.__color == 'yellow' and new_color == 'red')
        return True if condition else False

    def _switch_color(self, color, period):
        print(f"Цвет светофора: {self._traffic_light_colors[color]}")
        self.__previous_color, self.__color = self.__color, color
        time.sleep(period)

    def running(self, color):
        if not self._check_color_order(color):
            print("Ошибка! Неправильный порядок переключения")
            return
        if color == 'red':
            self._switch_color(color, 7)
        elif color == 'yellow':
            self._switch_color(color, 2)
        elif color == 'green':
            self._switch_color(color, 5)

    # непрерывная работа светофора
    def running_continuously(self):
        while True:
            self.running('red')
            self.running('yellow')
            self.running('green')
            self.running('yellow')


my_traffic_light = TrafficLight()
my_traffic_light.running('red')
my_traffic_light.running('yellow')
my_traffic_light.running('green')
my_traffic_light.running('red')
# my_traffic_light.running_continuously()  # вызов метода для непрерывной работы
