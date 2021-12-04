list_input = input('Введите элементы списка: ')

list_input_1 = list_input.split()
len_list =len(list_input_1)
a=0

if len_list > 1:
    while a < len_list - 1:
        b= list_input_1[a]
        list_input_1[a] = list_input_1[a+1]
        list_input_1[a+1] = b
        a += 2
print(list_input_1)
