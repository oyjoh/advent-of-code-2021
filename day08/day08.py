import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()
data = [d.split(' | ') for d in data]


def part_one(data):
    return sum(sum(len(x) in [2, 3, 4, 7] for x in line[1].split()) for line in data)


def decipher(set_list, nums):
    s_num = ''
    for num in nums:
        for t, val in set_list:
            if set(num) == t:
                s_num += str(val)
    return int(s_num)


def part_two(data):
    # ¯\_(ツ)_/¯

    cnt = 0

    for line in data:
        pattern = line[0].split()
        pattern.sort(key=len)

        set_list = []

        # 1
        set_list.append((set(pattern[0]), 1))
        # 4
        set_list.append((set(pattern[2]), 4))
        # 7
        set_list.append((set(pattern[1]), 7))
        # 8
        set_list.append((set(pattern[-1]), 8))

        # len 6
        len_6 = [set(x) for x in pattern if len(x) == 6]
        # 6
        for s in len_6:
            if len(set_list[0][0] - s) != 0:
                len_6.remove(s)
                set_list.append((s, 6))
        # 0
        for s in len_6:
            if len(set_list[1][0] - s) != 0:
                len_6.remove(s)
                set_list.append((s, 0))
        # 9
        set_list.append((len_6.pop(), 9))

        # len 5
        len_5 = [set(x) for x in pattern if len(x) == 5]
        # 3
        for s in len_5:
            if len(set_list[0][0] - s) == 0:
                len_5.remove(s)
                set_list.append((s, 3))
        # 5
        for s in len_5:
            if len(set_list[1][0] - s) == 1:
                len_5.remove(s)
                set_list.append((s, 5))
        # 2
        set_list.append((len_5.pop(), 2))

        cnt += decipher(set_list, line[1].split())

    return cnt


print(f'part one: {part_one(data)}')
print(f'part two: {part_two(data)}')
