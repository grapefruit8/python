with open('test_3.txt') as file:
    lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in lines:
        emp_info = line.split()
        employees.update({emp_info[0]: int(emp_info[1])})
        sum_salary += int(emp_info[1])

print(f'Средний оклад сотрудников {sum_salary / len(employees)} руб')

for x, y in employees.items():
    if y < 20000:
        print(f'Сотрудник с окладом менее 20000 руб:\n {x}: {y}')
