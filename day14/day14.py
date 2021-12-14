import os
from collections import defaultdict


input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()

template = [c for c in data[0]]
rules = data[2:]


def part_one(template, rules):
    rule_dict = defaultdict(str)
    for r in rules:
        f, t = r.split(' -> ')
        rule_dict[f] = t

    curr = template
    for _ in range(10):
        new_arr = [curr[0]]
        for i in range(len(curr)-1):
            pair = curr[i] + curr[i+1]
            if pair in rule_dict:
                new_arr += [rule_dict[pair], curr[i+1]]
            else:
                new_arr += [curr[i+1]]
        curr = new_arr
    return curr.count(max(curr, key=curr.count)) - curr.count(min(curr, key=curr.count))


def part_two(template, rules):
    rule_dict = defaultdict(str)
    for r in rules:
        f, t = r.split(' -> ')
        rule_dict[f] = t

    pair_dict = defaultdict(int)

    for i in range(len(template)-1):
        pair_dict[template[i]+template[i+1]] += 1

    for _ in range(40):
        insert = []
        for key in pair_dict:
            if key in rule_dict and pair_dict[key] > 0:
                val = pair_dict[key]
                pair_dict[key] -= val
                new_char = rule_dict[key]
                insert += [(key[0]+new_char, val), (new_char+key[1], val)]
        for i, val in insert:
            pair_dict[i] += val

    char_dict = defaultdict(int)

    for key in pair_dict:
        char_dict[key[1]] += pair_dict[key]

    all_values = char_dict.values()
    return (max(all_values) - min(all_values))-1


print(f'part one: {part_one(template, rules)}')
print(f'part two: {part_two(template, rules)}')
