with open('test_2.txt', 'r') as file:
    lines = file.readlines()
    print(f'Всего строк: {len(lines)}')
    for key, value in enumerate(lines):
        word = value.split(' ')
        print(f'Слов в строке {key + 1} : {len(word)}')
    