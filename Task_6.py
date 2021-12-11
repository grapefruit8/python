from itertools import count, cycle

user_input = int(input('Введите целое число: '))
for i in count(user_input):
    if i > 10:
        break
    else:
        print(i)

user_input_2 = list(input('Введите элементы списка: ').split())
a = 0
for value in cycle(user_input_2):
    if a > 10:
        break
    print(value)
    a += 1
