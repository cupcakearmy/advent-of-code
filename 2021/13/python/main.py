#!/usr/bin/env python

from os.path import dirname, join
from typing import Tuple

# Day 13

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Paper:
    def __init__(self, points: set[tuple[int, int]], folds=list[tuple[bool, int]]):
        self.points = points
        self.folds = folds

    def __str__(self):
        max_x = 0
        max_y = 0
        for x, y in self.points:
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        # Init grid
        grid = [
            ['.' for _ in range(max_x+1)]
            for _ in range(max_y+1)
        ]

        # Fill grid
        for x, y in self.points:
            grid[y][x] = '#'

        return '\n'.join([
            ''.join(row)
            for row in grid
        ])

    def fold_all(self):
        for fold in self.folds:
            self.fold(fold)

    def fold(self, fold):
        x, threshold = fold
        i = 0 if x else 1
        for point in list(self.points):
            value = point[i]
            if value < threshold:
                continue
            new_value = 2*threshold - value
            self.points.remove(point)
            p = list(point)
            p[i] = new_value
            self.points.add(tuple(p))

    def flag_1(self):
        self.fold(self.folds[0])
        print(len(self.points))

    def flag_2(self):
        self.fold_all()
        print(self)

    @staticmethod
    def parse(data: str) -> 'Paper':
        header, footer = data.split('\n\n')
        points = {
            tuple(map(int, point.split(',')))
            for point
            in header.split('\n')
        }

        folds = [
            (fold[11] == 'x', int(fold[13:]))
            for fold in footer.split('\n')
        ]
        return Paper(points, folds)

        # 1
print('1.')
paper = Paper.parse(test)
paper.flag_1()
paper = Paper.parse(data)
paper.flag_1()


# 2
print('\n2.')
paper = Paper.parse(test)
paper.flag_2()
paper = Paper.parse(data)
paper.flag_2()
