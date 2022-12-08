#!/usr/bin/env python

from dataclasses import dataclass
from functools import reduce
from os.path import dirname, join

# Day 08

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass
class Forest:
    grid: list[list[int]]
    size: int

    def is_tree_visible(self, y: int, x: int) -> tuple[bool, int]:
        value = self.grid[y][x]
        combinations = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visible = 4
        views: list[int] = []
        for dy, dx in combinations:
            X = x
            Y = y
            view = 0
            while True:
                X += dx
                Y += dy
                # Gone outside the forest, so must be visible
                if Y < 0 or Y == self.size or X < 0 or X == self.size:
                    break
                view += 1
                if value <= self.grid[Y][X]:
                    visible -= 1
                    break
            views.append(view)

        score = reduce(lambda a, b: a*b, views, 1)
        return visible > 0, score

    def analyze(self) -> tuple[int, int]:
        visible = 0
        best = 0
        for y in range(self.size):
            for x in range(self.size):
                is_visible, score = self.is_tree_visible(y, x)
                if is_visible:
                    visible += 1
                if score > best:
                    best = score
        return visible, best

    @staticmethod
    def parse(data: str):
        lines = data.split()
        size = len(lines)
        grid = [
            [int(lines[y][x]) for x in range(size)]
            for y in range(size)
        ]
        return Forest(grid, size)


forest = Forest.parse(test)
print(forest.analyze())

forest = Forest.parse(data)
print(forest.analyze())
