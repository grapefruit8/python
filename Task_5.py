user_input = int(input('Ваша оценка: '))
my_list = [9, 8, 8, 7, 5, 5, 3, 2]
a = False
for index, elem in enumerate(my_list):
    if user_input > elem:
        my_list.insert(index, user_input)
        a = True
        break
if not a:
    my_list.append(user_input)

print(my_list)
