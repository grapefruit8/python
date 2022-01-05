class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите число: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise ZeroError("Делить на ноль нельзя!")
        else:
            result = user_num_1 / user_num_2
            return result
    except ValueError:
        return "Вы ввели не число"
    except ZeroError as err:
        return err


print(div())
