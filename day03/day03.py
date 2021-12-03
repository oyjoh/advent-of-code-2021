import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def part_one(data):
    zero_cnt = [0] * len(data[0])
    one_cnt = [0] * len(data[0])

    for line in data:
        for idx, c in enumerate(line):
            if c == '1':
                one_cnt[idx] += 1
            else:
                zero_cnt[idx] += 1

    gamma, epsilon = '', ''

    for i in range(len(zero_cnt)):
        if zero_cnt[i] > one_cnt[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)


def count_bits(data, idx):
    zero_cnt, one_cnt = 0, 0

    for line in data:
        if line[idx] == '1':
            one_cnt += 1
        else:
            zero_cnt += 1
    return zero_cnt, one_cnt


def most_frequent(data, idx):
    zero_cnt, one_cnt = count_bits(data, idx)
    return '1' if one_cnt >= zero_cnt else '0'


def least_frequent(data, idx):
    zero_cnt, one_cnt = count_bits(data, idx)
    return '0' if one_cnt >= zero_cnt else '1'


def part_two(data):
    oxy, co2 = set(data), set(data)
    oxy_bin, co2_bin = '', ''

    for i in range(len(data[0])):
        cnt_oxy = most_frequent(oxy, i)
        cnt_co2 = least_frequent(co2, i)

        for line in data:
            if line[i] != cnt_co2:
                co2.discard(line)
            if line[i] != cnt_oxy:
                oxy.discard(line)

        if len(oxy) == 1:
            oxy_bin = oxy.pop()
        if len(co2) == 1:
            co2_bin = co2.pop()

    return int(co2_bin, 2) * int(oxy_bin, 2)


print(f'part one: {part_one(data)}')
print(f'part two: {part_two(data)}')
