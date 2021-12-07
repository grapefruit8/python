def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word

user_input = input('Введите слова разделенные пробелом: ').split(' ')
for word in user_input:
    print(f'{int_func(word)}', end=' ')
