profit = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))

if profit > costs:
    print('Компания работает с прибылью')
    revenue = (profit - costs) / profit * 100
    print(f'Рентабельность выручки {revenue:.2f}%')
    workers = int(input('Введите количество сотрудников: '))
    result = (profit - costs) / workers
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {result:.2f}')
elif profit == costs:
    print('Компания работает в ноль')
else:
    print('Компания работает в убыток')
