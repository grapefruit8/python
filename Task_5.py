def sum_list(nums_str, stop):
    sum_nums = 0
    for i in nums_str:
        if i == stop:
            break
        sum_nums += int(i)

    return sum_nums


symbol = '#'
finished = False
line =0

while not finished:
    input_user = input('Ведите числа через пробел: ').split(' ')
    line += sum_list(input_user, symbol)
    finished = symbol in input_user
    print(f'Сумма = {line}')
