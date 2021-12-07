import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def part_one(data):
    cost = sum(data)**2

    lower = min(data)
    upper = max(data)

    for i in range(lower, upper+1):
        c = 0
        for val in data:
            c += abs(val - i)
        cost = min(cost, c)

    return cost


def part_two(data):
    cost = sum(data)**2

    lower = min(data)
    upper = max(data)

    for i in range(lower, upper+1):
        c = 0
        for val in data:
            step = abs(val - i)
            c += ((step**2)+step) // 2
        cost = min(cost, c)

    return cost


data = list(map(int, data[0].split(',')))
print(f'part one: {part_one(data)}')
print(f'part two: {part_two(data)}')
