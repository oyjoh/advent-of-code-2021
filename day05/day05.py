import os

input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def create_line(x1, y1, x2, y2):
    l = max(abs(x2 - x1), abs(y2 - y1))
    dx = (x2 - x1) // l
    dy = (y2 - y1) // l

    line = []
    for _ in range(l+1):
        line.append((x1, y1))
        x1 += dx
        y1 += dy

    return line


def solve(coord):
    table = [[0 for _ in range(1000)] for _ in range(1000)]
    for a, b in coord:
        line = create_line(a[0], a[1], b[0], b[1])
        for p in line:
            table[p[1]][p[0]] += 1

    cnt = 0
    for row in table:
        for val in row:
            if val > 1:
                cnt += 1
    return cnt


coordinates = []
for line in data:
    a, b = line.split(' -> ')
    a_x, a_y = map(int, a.split(','))
    b_x, b_y = map(int, b.split(','))
    coordinates.append(((a_x, a_y), (b_x, b_y)))


print(
    f'part one: {solve(list(filter(lambda a: (a[0][0] == a[1][0] or a[0][1] == a[1][1]), coordinates)))}')
print(f'part two: {solve(coordinates)}')
