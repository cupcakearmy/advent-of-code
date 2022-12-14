#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join
from typing import Literal

# Day 14

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
        return Point(self.x+other.x, self.y+other.y)


@dataclass
class Cave:
    sand: set[Point]
    rocks: set[Point]
    boundaries: dict[Literal['max_y', 'max_x', 'min_x', 'min_y'], int]
    bottom: bool = False
    source: Point = Point(500, 0)

    def display(self):
        s = ''
        for y in range(self.boundaries['min_y'], self.boundaries['max_y']+1):
            s += '\n'
            for x in range(self.boundaries['min_x'], self.boundaries['max_x']+1):
                p = Point(x, y)
                if p == self.source:
                    s += '+'
                elif p in self.sand:
                    s += 'O'
                elif p in self.rocks:
                    s += '#'
                else:
                    s += '.'
        print(s)

    def produce(self) -> bool:
        movements = [Point(0, 1), Point(-1, 1), Point(1, 1)]
        sanddorn = self.source
        while True:
            moved = False
            for movement in movements:
                p = sanddorn + movement
                if p in self.sand or p in self.rocks:
                    continue
                if self.bottom and p.y == self.boundaries['max_y']+2:
                    continue
                else:
                    if not self.bottom and p.y >= self.boundaries['max_y']:
                        return False
                    sanddorn = p
                    moved = True
                    break
            if not moved:
                self.sand.add(sanddorn)
                return self.source != sanddorn

    def simulate(self):
        while self.produce():
            pass
        return len(self.sand)

    @ staticmethod
    def parse(data: str, bottom=False) -> 'Cave':
        rocks = [[[
            int(coordinate)
            for coordinate in segment.split(',')]
            for segment in rock.split(' -> ')]
            for rock in data.splitlines()]
        points: set[Point] = set()
        xs: list[int] = []
        ys: list[int] = []
        for rock in rocks:
            for i in range(len(rock)-1):
                a, b = rock[i], rock[i+1]
                x_min, y_min = min(a[0], b[0]), min(a[1], b[1])
                for dx in range(x_min, x_min + abs(a[0]-b[0])+1):
                    for dy in range(y_min, y_min + abs(a[1]-b[1])+1):
                        xs.append(dx)
                        ys.append(dy)
                        points.add(Point(dx, dy))
        return Cave(set(), points, {'min_y': 0, 'max_y': max(ys), 'min_x': min(xs), 'max_x': max(xs)}, bottom)


# Running
cave = Cave.parse(data, bottom=True)
print(cave.simulate())
