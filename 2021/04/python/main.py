#!/usr/bin/env python

from os.path import join, dirname
from typing import List

# Day 04

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Board:
    def __init__(self, raw: str) -> None:
        self.matrix = [
            [int(x) for x in row.split(' ') if x != '']
            for row in raw.split('\n')
        ]
        self.chosen = [
            [False for _ in range(len(self.matrix))]
            for _ in range(len(self.matrix))
        ]

    def enter(self, number: int):
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                if col == number:
                    self.chosen[i][j] = True

    def bingo(self):
        for row in self.chosen:
            if all(row):
                return True
        for i in range(len(self.chosen)):
            if all([row[i] for row in self.chosen]):
                return True
        return False

    def flag(self, number: int) -> int:
        numbers = []
        for i, row in enumerate(self.chosen):
            for j, col in enumerate(row):
                if not col:
                    numbers.append(self.matrix[i][j])
        total = sum(numbers)
        # print(f'Flag: {total} {number}')
        return total*number

    def __str__(self):
        numbers = '\n'.join([' '.join([str(x) for x in row])
                            for row in self.matrix])
        chosen = '\n'.join([' '.join([str(x) for x in row])
                           for row in self.chosen])
        return f'{numbers}\n{chosen}'


class Bingo:
    def __init__(self, raw: str) -> None:
        numbers, *boards = raw.split('\n\n')
        self.dice = [int(x) for x in numbers.strip().split(',')]
        self.boards = [Board(board) for board in boards]

    def play(self, to_win=True):
        for number in self.dice:
            finished: List[Board] = []
            for board in self.boards:
                board.enter(number)
                if board.bingo():
                    if to_win:
                        return board.flag(number)
                    else:
                        if len(self.boards) == 1:
                            return board.flag(number)
                        else:
                            finished.append(board)
            if finished:
                for board in finished:
                    self.boards.remove(board)

    def __str__(self):
        return '\n\n'.join([str(board) for board in self.boards])


# 1
print('1.')

bingo = Bingo(test)
result = bingo.play()
print(f"Test: {result}")

bingo = Bingo(data)
result = bingo.play()
print(f"Result: {result}")


# 2
print('2.')

bingo = Bingo(test)
result = bingo.play(to_win=False)
print(f"Test: {result}")

bingo = Bingo(data)
result = bingo.play(to_win=False)
print(f"Result: {result}")
