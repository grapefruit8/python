user_input = input('Введите строку: ')

a = user_input.split()
for num, word in enumerate(a):
    if len(word) > 10:
        word = word[0:10]
    print(f'{num+1} - {word}')
