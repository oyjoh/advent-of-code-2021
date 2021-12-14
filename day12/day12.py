import os
from collections import defaultdict

input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()


def part_one(root, graph, visited):
    if root.islower() and root != 'end':
        visited.append(root)
    cnt = 0
    if root == 'end':
        cnt += 1
    else:
        for adj in graph[root]:
            if adj not in visited:
                cnt += part_one(adj, graph, [] + visited)

    return cnt


def part_two(root, graph, visited, double):
    if root.islower() and root != 'end':
        visited.append(root)
    cnt = 0
    if root == 'end':
        cnt += 1
    else:
        for adj in graph[root]:
            if adj not in visited:
                cnt += part_two(adj, graph, [] + visited, double)
            if adj in visited and double and adj != 'start':

                cnt += part_two(adj, graph, [] + visited, False)

    return cnt


graph = defaultdict(list)

for line in data:
    a, b = line.split('-')
    graph[a].append(b)
    graph[b].append(a)


part1 = part_one('start', graph, [])
part2 = part_two('start', graph, [], True)

print(f'part one: {part1}')
print(f'part two: {part2}')
