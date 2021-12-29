class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_mass(self, mass_1m2: int, thickness: int):
        mass = self._length * self._width * mass_1m2 * thickness // 1000
        return mass


road = Road(5000, 20)
print(road.get_mass(25, 5))
