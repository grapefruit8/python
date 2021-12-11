from sys import argv

output = int(argv[1])
rate = int(argv[2])
premium = int(argv[3])


def wage_sum():
    print((output * rate) + premium)


wage_sum()
