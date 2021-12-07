def my_func(x, y):
    if x < 0:
        return 'Число не может быть меньше 0'
    if y > 0:
        return 'Число не может быть больше 0'
    else:
        deg = x ** y
    return deg


x = float(input('Введите положительное число: '))
y = int(input('Введите отрицательную степень: '))
print(my_func(x, y))
