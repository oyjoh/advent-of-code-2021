import os
input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()

incomplete = []


def part_one(data):
    point_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    pair = {')': '(',  ']': '[', '}': '{', '>': '<'}

    p_cnt = 0

    for line in data:
        stack = []
        for c in line:
            if c in [')', ']', '}', '>']:
                if pair[c] == stack[-1]:
                    tmp = stack.pop()
                else:
                    stack.append(c)
                    p_cnt += point_dict[c]
                    break
            else:
                stack.append(c)

        if all(s not in [')', ']', '}', '>'] for s in stack):
            incomplete.append(line)

    return p_cnt


def part_two():
    point_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    pair = {')': '(',  ']': '[', '}': '{', '>': '<'}
    pair2 = {'{': '}', '(': ')', '[': ']', '<': '>'}

    scores = []

    for line in incomplete:
        stack = []
        for c in line:
            if c in [')', ']', '}', '>']:
                if pair[c] == stack[-1]:
                    tmp = stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        cnt = 0
        for i in reversed(stack):
            cnt = cnt * 5
            cnt += point_dict[pair2[i]]
        scores.append(cnt)

    return sorted(scores)[(len(scores)-1)//2]


print(f'part one: {part_one(data)}')
print(f'part two: {part_two()}')
