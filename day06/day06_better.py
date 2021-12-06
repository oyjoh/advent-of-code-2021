import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()
data = list(map(int, data[0].split(',')))


def solve(data, days):
    table = [0 for _ in range(9)]
    for val in data:
        table[val] += 1

    idx = 6
    for _ in range(days):
        idx = (idx + 1) % 9
        table[idx] += table[(idx + 2) % 9]

    return(sum(table))


print(f'part one: {solve(data, 80)}')
print(f'part two: {solve(data, 256)}')
