from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]

result = reduce(lambda prev, cur: prev * cur, my_list)

print(result)
