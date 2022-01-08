import random

with open('test_5.txt', 'w') as file:
    for _ in range(20):
        file.write(f'{random.randint(0,10)} ')

with open('test_5.txt', 'r') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split()
    print(f"Содержимое файла:\n {numbers_str}")
    print(f"Сумма чисел:\n {sum([int(i) for i in numbers_lst])}")
    