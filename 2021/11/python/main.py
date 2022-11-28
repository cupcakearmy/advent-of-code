#!/usr/bin/env python

from os.path import dirname, join

# Day 11

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


def bold(text: str) -> str:
    return f'\033[1m{text}\033[0m'


def red(text: str) -> str:
    return f'\033[31m{text}\033[0m'


class OctoGrid:

    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.flashed = set()
        self.x = len(grid[0])
        self.y = len(grid)

    def _flash(self, x: int, y: int):
        if (x, y) in self.flashed:
            return False
        self.flashed.add((x, y))
        # print(f"Flash at {y}, {x}")
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                # if dx == dy == 0:
                #     continue
                target_x = x + dx
                target_y = y + dy
                if 0 <= target_x < self.x and 0 <= target_y < self.y:
                    self.grid[target_y][target_x] += 1
        return True

    def _check(self):
        for y in range(self.y):
            for x in range(self.x):
                if self.grid[y][x] > 9:
                    if self._flash(x, y):
                        return True
        return False

    def _step(self):
        self.flashed.clear()

        # Increase all by one
        for y in range(self.y):
            for x in range(self.x):
                self.grid[y][x] += 1

        while self._check():
            pass

        for y in range(self.y):
            for x in range(self.x):
                if self.grid[y][x] > 9:
                    self.grid[y][x] = 0

        return len(self.flashed)

    def count_flashes(self, steps):
        total = 0
        for _ in range(steps):
            total += self._step()
        return total

    def first_simultaneous(self):
        step = 0
        while True:
            step += 1
            if self._step() == self.y * self.x:
                return step

    def __str__(self) -> str:
        def f(x):
            s = str(x).ljust(3, ' ')
            if x > 9:
                s = bold(red(s))
            return s
        s = ''
        for y in range(self.y):
            s += ''.join(f(x) for x in self.grid[y]) + '\n'
        return s

    @staticmethod
    def parse(data):
        grid = [
            list(map(int, line))
            for line
            in data.splitlines()
        ]
        return OctoGrid(grid)


        # 1
print('1.')

grid = OctoGrid.parse(test)
print(grid.count_flashes(100))
grid = OctoGrid.parse(test)
print(grid.first_simultaneous())

# 2
print('\n2.')

grid = OctoGrid.parse(data)
print(grid.count_flashes(100))
grid = OctoGrid.parse(data)
print(grid.first_simultaneous())
