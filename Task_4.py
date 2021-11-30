user_number = int(input('Введите целое положительное число: '))
max = 0

while user_number > 0:
    if user_number % 10 > max:
        max = user_number % 10
    user_number = user_number // 10
print(f'Cамая большая цифра в числе: {max}')
