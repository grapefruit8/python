class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Go!')

    def stop(self):
        print(f'Stop!')

    def turn(self, direction):
        print(f'{self.name} changed direction to the {direction}!')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speeding!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speeding!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(80, 'red', 'Town car')
car_2 = SportCar(160, 'blue', 'Sport car')
car_3 = WorkCar(60, 'grey', 'Work car')
car_4 = PoliceCar(100, 'white', 'Police car')

car_1.show_speed()
car_3.show_speed()

car_1.speed = 55
car_1.show_speed()

car_2.turn('Left')
