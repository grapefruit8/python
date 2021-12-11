first_list = [1, 200, 40, 15, 30, 7, 215, 80, 90, 8]
list_result = [a for i, b in enumerate(first_list) for a in first_list[i+1:i+2] if a > b]

print(list_result)
