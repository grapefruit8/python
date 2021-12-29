class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


test = Position('Иван', 'Иванов', 'Художник', 30000, 15000)
print(test.name)
print(test.surname)
print(test.position)
print(test._income)
print(test.get_full_name())
print(test.get_total_income())
