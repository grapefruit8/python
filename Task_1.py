with open('test.txt', 'w') as file:
    user_input = input('Введите данные :\n')
    while user_input:
        file.write(f'{user_input}\n')
        user_input = input('Введите данные :\n')
