# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod


class WrongEquipmentTypeError(Exception):
    pass


class WrongDepartmentTypeError(Exception):
    pass


class WrongQuantityTypeError(Exception):
    pass


class AbstractOfficeEquipment(ABC):
    def __init__(self, model, brand, serial_number):
        self._model = model
        self._brand = brand
        self._serial_number = serial_number

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def serial_number(self):
        return self._serial_number

    @property
    @abstractmethod
    def equipment_type(self):
        pass


class Scanner(AbstractOfficeEquipment):
    equipment_type = "Сканер"


class Printer(AbstractOfficeEquipment):
    equipment_type = "Принтер"


class MFD(AbstractOfficeEquipment):
    equipment_type = "МФУ"


class AbstractEquipmentWarehouse(ABC):
    def __init__(self, name):
        self._warehouse_name = name
        self._equipment = {}

    @staticmethod
    def _validate_office_equipment(data):
        if not isinstance(data, (list, tuple, AbstractOfficeEquipment)):
            raise WrongEquipmentTypeError

        if not isinstance(data, AbstractOfficeEquipment):
            for d in data:
                if not isinstance(d, AbstractOfficeEquipment):
                    raise WrongEquipmentTypeError

    @staticmethod
    def _validate_department(data):
        if not isinstance(data, AbstractEquipmentWarehouse):
            raise WrongDepartmentTypeError

    @staticmethod
    def _validate_quantity(data):
        if not isinstance(data, (int, float)):
            raise WrongQuantityTypeError

    def add(self, item):
        """
        Получение техники на склад

        :param item: single AbstractOfficeEquipment instance or collection of instances (list or tuple)
        :return: bool
        """

        if isinstance(item, AbstractOfficeEquipment):
            item = [item]
        try:
            self._validate_office_equipment(item)
        except WrongEquipmentTypeError:
            print(f"Ошибка: неправильный тип данных техники. "
                  f"Не могу добавить технику на склад '{self._warehouse_name}'")
            return False

        print(f"\nНа склад '{self._warehouse_name}' добавлены слеующие единицы техники:")
        for d in item:
            self._equipment.setdefault(d.equipment_type, []).append(d)
            print(f"{d.equipment_type} {d.brand} {d.model}, серийный номер: {d.serial_number}")
        return True

    def move_equipment(self, department, equipment_type, brand=None,
                       model=None, serial_number=None, quantity=1):
        """
        Передача техники в подразделение (на склад подразделения или основной склад)
        Если не введён серийный номер, ищем указанное количиство техники с подходящими параметрами
        """

        try:
            self._validate_department(department)
            self._validate_quantity(quantity)
        except WrongDepartmentTypeError:
            print("Ошибка: неправильный тип данных подразделения. Перемещение невозможно")
            return
        except WrongQuantityTypeError:
            print("Ошибка: неправильный тип введённого количества. Перемещение невозможно")
            return
        except Exception as e:
            print(f"Ошибка: {e}")
            return
        if quantity < 1:
            print("Ошибка: количества не может быть меньше 1. Перемещение невозможно")
            return

        print("Перемещаю технику со склада")
        if serial_number is not None:
            quantity = 1
        to_move = []
        to_delete = []

        for i, item in enumerate(self._equipment[equipment_type]):
            if (
                    brand is None or item.brand == brand and
                    model is None or item.model == model and
                    serial_number is None or item.serial_number == serial_number
            ):
                to_move.append(item)
                to_delete.append(i)
                quantity -= 1
            if not quantity:
                break
        else:
            print(f"Ошибка: подходящая техника на складе не найдена. Перемещение невозможно")
            return

        if department.add(to_move):
            for i in to_delete:
                del self._equipment[equipment_type][i]
            print("Перемещение завершено успешно")

    def show_warehouse_equipment(self):
        print(f"\nТовары на складе {self._warehouse_name}:")
        if not len(self._equipment.values()):
            print("Склад пуст")
            return

        for equipment_type, devices in self._equipment.items():
            for d in devices:
                print(f"{d.equipment_type} {d.brand} {d.model}, "
                      f"серийный номер: {d.serial_number}")
            print(f"Итого техники типа '{equipment_type}': {len(devices)} шт.")
        print(f"Итого техники типа на складе: {len(self._equipment.values())} шт.")


class MainWarehouse(AbstractEquipmentWarehouse):
    def remove(self, equipment_type, brand, model, serial_number):
        """
        Списание техники со склада
        """

        for i, item in enumerate(self._equipment[equipment_type]):
            if item.brand == brand and item.model == model and item.serial_number == serial_number:
                del self._equipment[equipment_type][i]
                print(f"Произведено списание со склада: "
                      f"{equipment_type} {brand} {model}, серийный номер: {serial_number}")
                return
        print("Списание не выполнено. Техника не найдена на складе")


class DepartmentWarehouse(AbstractEquipmentWarehouse):
    pass


if __name__ == '__main__':
    pass
