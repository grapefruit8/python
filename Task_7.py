class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение: {self.a * other.a - (self.b * other.b)} + {self.a * other.b + (self.b * other.a)} * i'


x_1 = ComplexNumber(2, 5)
x_2 = ComplexNumber(3, 6)
print(x_1 + x_2)
print(x_1 * x_2)
