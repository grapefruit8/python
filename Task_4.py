new_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test_4.txt') as file, open('new_test_4.txt', 'w') as new_file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        ru_nums = new_dict.get(data[0])
        new_file.write(f'{line.replace(data[0], ru_nums)}')
