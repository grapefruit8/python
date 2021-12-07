def my_func(number_1, number_2, number_3):
    sum = number_1 + number_2 + number_3
    return sum - min(number_1, number_2, number_3)


input_user_1 = int(input('First number: '))
input_user_2 = int(input('Second number: '))
input_user_3 = int(input('Second number: '))
result = my_func(input_user_1, input_user_2, input_user_3)
print(result)
