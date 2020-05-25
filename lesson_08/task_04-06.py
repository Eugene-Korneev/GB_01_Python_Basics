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

from abc import ABC


class WrongEquipmentTypeError(Exception):
    pass


class WrongDepartmentTypeError(Exception):
    pass


class WrongQuantityTypeError(Exception):
    pass


class AbstractOfficeEquipment(ABC):
    equipment_type: str

    def __init__(self, brand, model, serial_number):
        self._model = model
        self._brand = brand
        self._serial_number = serial_number

    # to depress pycharm warning
    def __iter__(self):
        pass

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def serial_number(self):
        return self._serial_number


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

        print(f"\nПроизвожу добавление техники на склад '{self._warehouse_name}'")
        if isinstance(item, AbstractOfficeEquipment):
            item = [item]
        try:
            self._validate_office_equipment(item)
        except WrongEquipmentTypeError:
            print(f"Ошибка: неправильный тип данных техники. "
                  f"Не могу добавить технику на склад")
            return False

        print(f"На склад '{self._warehouse_name}' добавлены слеующие единицы техники:")
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

        print(f"\nПроизвожу перемещение техники со склада '{self._warehouse_name}'")
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
            print("Ошибка: количество не может быть меньше 1. Перемещение невозможно")
            return

        if serial_number is not None:
            quantity = 1
        to_move = []
        to_delete = []

        for i, item in enumerate(self._equipment[equipment_type]):
            if (
                    (brand is None or item.brand == brand) and
                    (model is None or item.model == model) and
                    (serial_number is None or item.serial_number == serial_number)
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
            if not self._equipment[equipment_type]:
                del self._equipment[equipment_type]
            print("Перемещение завершено успешно")

    def show_warehouse_equipment(self):
        print(f"\nТехника на складе '{self._warehouse_name}':")
        if not len(self._equipment.values()):
            print("Склад пуст")
            return

        total_qty = 0
        for equipment_type, devices in self._equipment.items():
            for d in devices:
                print(f"{d.equipment_type} {d.brand} {d.model}, "
                      f"серийный номер: {d.serial_number}")
            total_qty += len(devices)
            print(f"Итого техники типа '{equipment_type}': {len(devices)} шт.")
        print(f"Итого техники на складе: {total_qty} шт.")


class MainWarehouse(AbstractEquipmentWarehouse):
    def remove(self, equipment_type, brand, model, serial_number):
        """
        Списание техники со склада
        """

        print(f"\nПроизвожу списание со склада '{self._warehouse_name}':")
        for i, item in enumerate(self._equipment.get(equipment_type, [])):
            if item.brand == brand and item.model == model and item.serial_number == serial_number:
                del self._equipment[equipment_type][i]
                if not self._equipment[equipment_type]:
                    del self._equipment[equipment_type]
                print(f"Произведено списание со склада: "
                      f"{equipment_type} {brand} {model}, серийный номер: {serial_number}")
                return
        print(f"Списание не выполнено. Техника не найдена на складе")


class DepartmentWarehouse(AbstractEquipmentWarehouse):
    pass


if __name__ == '__main__':
    main_warehouse = MainWarehouse('Основной склад')
    it_department = DepartmentWarehouse('Подразделение IT')
    sales_department = DepartmentWarehouse('Отдел продаж')
    shopping_department = DepartmentWarehouse('Магазин')
    main_warehouse.show_warehouse_equipment()

    printer_1 = Printer("Canon", 'PIXMA TR8520', 'P001')
    printer_2 = Printer("Canon", 'PIXMA TR8520', 'P002')
    main_warehouse.add(printer_1)
    main_warehouse.show_warehouse_equipment()

    printer_3 = Printer("HP", 'Color Laser 150A', 'P003')
    printer_4 = Printer("Kyocera", 'ECOSYS P3150DN', 'P004')
    scanner_1 = Scanner("Epson", 'Perfection V370', 'S001')
    scanner_2 = Scanner("Canon", 'CanoScan LiDE 300', 'S002')
    scanner_3 = Scanner("HP", 'ScanJet Pro 2000 s1', 'S003')
    mfd_1 = MFD("Kyocera", 'ECOSYS M3645DN', 'M001')
    mfd_2 = MFD("Xerox", 'VersaLink B405', 'M002')
    equipment = (printer_2, printer_3, printer_4, scanner_1, scanner_2,
                 scanner_3, mfd_1, mfd_2)
    main_warehouse.add(equipment)
    main_warehouse.show_warehouse_equipment()

    main_warehouse.move_equipment(it_department, 'МФУ', 'Kyocera')
    it_department.show_warehouse_equipment()

    main_warehouse.move_equipment(sales_department, 'Принтер', serial_number='P003')
    main_warehouse.move_equipment(sales_department, 'Сканер', 'Epson', 'Perfection V370')
    sales_department.show_warehouse_equipment()

    main_warehouse.move_equipment(shopping_department, 'Принтер', 'Canon', quantity=2)
    main_warehouse.move_equipment(shopping_department, 'Сканер', 'Canon')
    shopping_department.show_warehouse_equipment()
    main_warehouse.show_warehouse_equipment()

    main_warehouse.remove('Сканер', 'HP', 'ScanJet Pro 2000 s1', 'S003')
    main_warehouse.show_warehouse_equipment()
