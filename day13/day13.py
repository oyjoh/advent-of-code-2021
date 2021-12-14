import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def solve(table, instructions):
    y_limit = len(table)
    x_limit = len(table[0])

    for idx, inst in enumerate(instructions):
        ax, pos = inst
        if ax == 'x':
            for y in range(y_limit):
                fold = list(reversed(table[y][pos+1:x_limit]))
                for i, x in enumerate(range(pos-len(fold), pos)):
                    table[y][x] = max(table[y][x], fold[i])
            x_limit = pos
        else:

            fold = list(reversed(table[pos+1:y_limit]))
            for i, y in enumerate(range(pos-len(fold), pos)):
                for x in range(x_limit):
                    table[y][x] = max(table[y][x], fold[i][x])

            y_limit = pos

        if idx == 0:
            score = 0
            for y in range(y_limit):
                for x in range(x_limit):
                    score += table[y][x]
            print(f'part one: {score}')

    print(f'part two:')
    for line in table[:y_limit]:
        s = ''
        for char in line[:x_limit]:
            if char == 0:
                s += ' '
            else:
                s += '#'
        print(s)

    score = 0
    for y in range(y_limit):
        for x in range(x_limit):
            score += table[y][x]

    return score


data_split = [data[: data.index('')], data[data.index('') + 1:]]

coords = []
max_x, max_y = 0, 0
for line in data_split[0]:
    x, y = map(int, line.split(','))
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    coords.append((x, y))

table = [[0 if (x, y) not in coords else 1 for x in range(max_x + 1)]
         for y in range(max_y+1)]

instructions = []
for line in data_split[1]:
    _, _, i = line.split()
    ax, val = i.split('=')
    instructions.append((ax, int(val)))


solve(table, instructions)
