import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


data = [[int(x) for x in i] for i in data]


def valid_coord(y, x):
    return len(data[0]) > x >= 0 and len(data) > y >= 0


def flash(y, x, data, rnd_set):
    rnd_set.add((y, x))
    data[y][x] = 0

    delta = [(y-1, x), (y+1, x), (y, x-1), (y, x+1),
             (y+1, x+1), (y+1, x-1), (y-1, x+1), (y-1, x-1)]

    for dy, dx in delta:
        if valid_coord(dy, dx) and (dy, dx) not in rnd_set:
            data[dy][dx] += 1
            if data[dy][dx] > 9:
                flash(dy, dx, data, rnd_set)


def part_one(data):

    cnt = 0
    for i in range(100):
        rnd_set = set()

        for y in range(len(data)):
            for x in range(len(data[0])):
                data[y][x] += 1

        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] > 9:
                    flash(y, x, data, rnd_set)

        for line in data:
            for val in line:
                if val == 0:
                    cnt += 1

    return cnt


def part_two(data):
    cnt = 0
    for i in range(10000):
        rnd_set = set()

        for y in range(len(data)):
            for x in range(len(data[0])):
                data[y][x] += 1

        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] > 9:
                    flash(y, x, data, rnd_set)

        rnd_sum = 0
        for line in data:
            for val in line:
                rnd_sum += val

        if rnd_sum == 0:
            return i + 1

    return -1


print(f'part one: {part_one([[x for x in l] for l in data])}')
print(f'part two: {part_two([[x for x in l] for l in data])}')
