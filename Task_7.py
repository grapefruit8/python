import json

companies = {}
pos_count, pos_sum = 0, 0
with open('test_7.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        profit = int(data[2]) - int(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            pos_count += 1
            pos_sum += profit

av_profit = pos_sum / pos_count
result = [companies, {'Average profit': av_profit}]

with open('result.json', 'w') as file:
    json.dump(result, file)
