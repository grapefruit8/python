def fact(n_):
    temp = 1
    for i in range(1, n_ + 1):
        temp *= i
        yield temp


n = int(input('Получение факториала числа: '))

for el in fact(n):
    print(el)
