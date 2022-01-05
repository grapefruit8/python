class NewError(Exception):
    def __init__(self, txt):
        self.txt = txt


def chek_element(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NewError(f'Ошибка: {string} - не число! ')


input_txt = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'stop'")
while input_txt != 'stop':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(chek_element(input_txt))
        counter += 1
    except NewError as e:
        if input_txt != 'stop':
            print(e.txt)

print(f"Содержимое списка:\n{numbers_list}")
