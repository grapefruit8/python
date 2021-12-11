first_list = [1, 2, 2, 7, 10, 10, 5, 21, 4, 4, 4, 20]

next_list = [i for i in first_list if first_list.count(i) == 1]

print(next_list)
