import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def part_one(data):
    fwd = 0
    depth = 0

    for line in data:
        dir, val = line.split()
        if dir == 'up':
            depth -= int(val)
        elif dir == 'down':
            depth += int(val)
        else:
            fwd += int(val)
    return fwd * depth


def part_two(data):
    fwd = 0
    depth = 0
    aim = 0

    for line in data:
        dir, val = line.split()
        if dir == 'up':
            aim -= int(val)
        elif dir == 'down':
            aim += int(val)
        else:
            fwd += int(val)
            depth += aim * int(val)
    return fwd * depth


print(part_one(data))
print(part_two(data))
