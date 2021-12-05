import os
import re

input = f'{os.path.basename(os.getcwd())}.txt'

data = open(input, 'r').read().splitlines()
input_board = data[1:]

drawn_numbers = list(map(int, data[0].split(',')))

input_board = [input_board[i * 6:(i + 1) * 6]
               for i in range((len(input_board) + 6 - 1) // 6)]


boards = []
for b in input_board:
    board = []

    for i in range(1, len(b)):
        board.append(list(map(int, b[i].split())))

    boards.append(board)


def count_unmarked(board):
    cnt = 0
    for row in board:
        for num in row:
            if num != -1:
                cnt += num
    return cnt


def win_check(board):
    for row in board:
        if sum(row) == -5:
            return count_unmarked(board)

    for col in range(5):
        if board[0][col] + board[1][col] + board[2][col] + board[3][col] + board[4][col] == -5:
            return count_unmarked(board)

    return -1


def part_one():

    for num in drawn_numbers:

        for bd in boards:
            for row_idx, row in enumerate(bd):
                if num in row:
                    col_idx = row.index(num)
                    bd[row_idx][col_idx] = -1
                    unmark_sum = win_check(bd)
                    if unmark_sum != -1:
                        return(unmark_sum*num)

    return('error')


def part_two(data):
    not_won_set = set()
    for idx, b in enumerate(boards):
        not_won_set.add(idx)

    for num in drawn_numbers:

        for bd_idx, bd in enumerate(boards):
            for row_idx, row in enumerate(bd):
                if num in row:
                    col_idx = row.index(num)
                    bd[row_idx][col_idx] = -1
                    unmark_sum = win_check(bd)

                    if unmark_sum != -1:
                        if bd_idx in not_won_set and len(not_won_set) == 1:
                            return(count_unmarked(bd)*num)
                        not_won_set.discard(bd_idx)

    return('error')


print(f'part one: {part_one()}')
print(f'part two: {part_two()}')
