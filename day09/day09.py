import os
from functools import reduce

input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


low_points = []


def valid_coord(y, x):
    return len(data[0]) > x >= 0 and len(data) > y >= 0


def part_one(data):
    cnt = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            n_vals = []
            delta = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

            for dy, dx in delta:
                if valid_coord(dy, dx):
                    n_vals.append(int(data[dy][dx]))

            if int(data[y][x]) < min(n_vals):
                cnt += int(data[y][x])+1
                low_points.append((y, x))  # (y,x)

    return cnt


def explore(p, visited):
    visited.add(p)
    s = 1
    y, x = p

    delta = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    for dy, dx in delta:
        if valid_coord(dy, dx) and (dy, dx) not in visited and data[dy][dx] != '9':
            s += explore((dy, dx), visited)

    return s


def part_two():
    basin_sizes = []
    for p in low_points:
        basin_sizes.append(explore(p, set()))

    return reduce((lambda x, y: x*y), sorted(basin_sizes)[-3:])


print(f'part one: {part_one(data)}')
print(f'part two: {part_two()}')
