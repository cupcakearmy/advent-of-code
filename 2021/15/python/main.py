#!/usr/bin/env python

from os.path import dirname, join

# Day 15

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Cavern:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.max_y = len(self.grid)
        self.max_x = len(self.grid[0])

    def __getitem__(self, index):
        x, y = index
        value = self.grid[y % self.max_y][x % self.max_x]
        extra = y // self.max_y + x // self.max_x
        if extra:
            value += extra
            value = ((value-1) % 9)+1
        return value

    def find_lowest_risk(self, factor=1):
        # Calculate lowest cost matrix
        matrix:  list[list[int]] = []
        dy = self.max_y*factor
        dx = self.max_x*factor

        for y in range(dy):
            matrix.append([])
            for x in range(dx):
                if x == 0 and y == 0:
                    matrix[y].append(0)
                    continue

                value = self[x, y]
                lowest = 0
                if y != 0:
                    lowest = matrix[y-1][x]
                if x != 0:
                    v = matrix[y][x-1]
                    if lowest == 0 or v < lowest:
                        lowest = v
                matrix[y].append(value + lowest)

        return matrix[dy-1][dx-1]

    @staticmethod
    def parse(data: str):
        grid = [
            [int(x) for x in y]
            for y in data.split('\n')
        ]
        return Cavern(grid)


        # 1
print('1.')

cavern = Cavern.parse(test)
print(cavern.find_lowest_risk())
cavern = Cavern.parse(data)
print(cavern.find_lowest_risk())

# 2
print('\n2.')
cavern = Cavern.parse(test)
print(cavern.find_lowest_risk(factor=5))
cavern = Cavern.parse(data)
print(cavern.find_lowest_risk(factor=5))
