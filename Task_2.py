def user_info(name, surname, year, city, email, tel):
    return f'{name} {surname} {year} {city} {email} {tel}'


a = input('Имя: ')
b = input('Фамилия: ')
c = input('Год рождения: ')
d = input('Город проживания: ')
e = input('Email: ')
f = input('Телефон: ')
result = user_info(name=a, surname=b, year=c, city=d, email=e, tel=f)
print(result)
