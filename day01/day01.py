import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()
data = list(map(int, data))


def part_one(data):
    cnt = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            cnt += 1
    return cnt


def part_two(data):
    cnt = 0
    for i in range(1, len(data)-2):
        if data[i] + data[i+1] + data[i+2] > data[i-1] + data[i] + data[i+1]:
            cnt += 1
    return cnt


print(part_one(data))
print(part_two(data))
