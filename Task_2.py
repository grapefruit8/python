user_number = int(input('Введите время в секундах: '))

hours = user_number // 3600
minutes = (user_number - hours * 3600) // 60
seconds = user_number - (hours * 3600 + minutes * 60)
result_str = f'Ваше время {hours:02}:{minutes:02}:{seconds:02}'

print(result_str)
