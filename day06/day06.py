import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()
data = list(map(int, data[0].split(',')))


def left_rotate(arr):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = tmp
    return arr


def solve(data, days):
    table = [0 for _ in range(9)]
    for val in data:
        table[val] += 1

    for _ in range(days):
        table = left_rotate(table)
        table[6] += table[8]

    return(sum(table))


print(f'part one: {solve(data, 80)}')
print(f'part two: {solve(data, 256)}')
