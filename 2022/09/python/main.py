#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join
from typing import Literal

# Day 09

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other: 'Point') -> int:
        return max(abs(self.x - other.x), abs(self.y-other.y))

    def normalise(self):
        self.x = max(-1, min(1, self.x))
        self.y = max(-1, min(1, self.y))
        return self


Directions = Literal['U', 'D', 'L', 'R']
Instruction = tuple[Directions, int]

MAPPING: dict[Directions, Point] = {'U': Point(0, 1), 'D': Point(0, -1), 'L': Point(-1, 0), 'R': Point(1, 0)}


class Rope:
    def __init__(self, instructions: list[Instruction], links: int) -> None:
        self.instructions = instructions
        start = Point(0, 0)
        self.touched: set[Point] = set([start])
        self.links = [start for _ in range(links)]

    def move(self, instruction: Instruction):
        direction, travel = instruction
        last = len(self.links) - 1
        for _ in range(travel):
            moved: list[Point] = []
            for i, link in enumerate(self.links):
                if i == 0:
                    link = link + MAPPING[direction]
                else:
                    head = moved[i-1]
                    distance = head.distance(link)
                    if distance > 1:
                        link = link + (head - link).normalise()
                moved.append(link)
                if i == last:
                    self.touched.add(link)
            self.links = moved

    def run(self):
        for instruction in self.instructions:
            self.move(instruction)
        return len(self.touched)

    @staticmethod
    def visualise(points: list[Point], numbered=True) -> str:
        """
        Only used to visualise, not actual logic
        """
        max_x = max(p.x for p in points)
        min_x = min(p.x for p in points)
        max_y = max(p.y for p in points)
        min_y = min(p.y for p in points)
        range_x = max_x - min_x
        range_y = max_y - min_y
        grid = [
            ['.' for _ in range(range_x+1)]
            for _ in range(range_y+1)
        ]
        for i, link in enumerate(points):
            row = grid[range_y-(link.y - min_y)]
            if row[link.x-min_x] == '.':
                row[link.x-min_x] = str(i) if numbered else "#"
        return '\n'.join(map(lambda line: ''.join(line), grid))

    @staticmethod
    def parse(data: str, links: int):
        instructions = [
            (i[0], int(i[1]))
            for i in map(lambda line: line.split(), data.splitlines())
        ]
        return Rope(instructions, links)


# Running
grid = Rope.parse(data, 2)
print(grid.run())
grid = Rope.parse(data, 10)
print(grid.run())
