def div_number(number_1, number_2):
    if number_2 == 0:
        return 'Вы не можете делить на 0'
    else:
        return number_1 / number_2

input_user_1 = int(input('First number: '))
input_user_2 = int(input('Second number: '))
result = div_number(input_user_1, input_user_2)
print(result)
