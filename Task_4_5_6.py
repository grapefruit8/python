class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, type, model, cost):
        self.type = type
        self.model = model
        self.cost = cost

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model, cost, colorful: bool):
        self.colorful = colorful
        super().__init__('Принтер', model, cost)


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, dpi):
        self.dpi = dpi
        super().__init__('Сканер', model, cost)


class Copier(OfficeEquipment):
    def __init__(self, model, cost, colorful: bool, dpi, velocity):
        self.colorful = colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('Ксерокс', model, cost)


if __name__ == '__main__':
    printer_1 = Printer('Epson', 8000, True)
    printer_2 = Printer('HP', 7000, False)
    scanner_1 = Scanner('Epson', 5000, '4800x4800')
    copier_1 = Copier('Canon', 5000, True, '1200x1200', 8)
    copier_2 = Copier('HP', 9000, False, '1200x1200', 16)

    warehouse = Warehouse()
    warehouse.push(printer_1)
    warehouse.push(printer_2)
    warehouse.push(scanner_1)
    warehouse.push(copier_1)
    warehouse.push(copier_2)

    warehouse.report_items()
    warehouse.report_total()
