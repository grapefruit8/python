user_input = input('Введите номер месяца: ')

a, b, c, d = 'Зима' , 'Весна' , 'Лето' , 'Осень'

month_list = [a, a, b, b, b, c, c, c, d, d, d, a]
print(month_list[int(user_input)-1])

month_dict = {'1': a, '2': a, '3': b, '4': b, '5': b, '6': c, '7': c, '8': c, '9': d, '10': d, '11': d, '12': a}
print(month_dict[user_input])
