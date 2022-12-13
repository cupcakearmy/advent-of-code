#!/usr/bin/env python

from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from os.path import dirname, join

# Day 12

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass(unsafe_hash=True)
class Point:
    y: int
    x: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.y+other.y, self.x+other.x)

    def distance(self, other: 'Point') -> int:
        return int(((self.y-other.y)**2 + (self.x-other.x)**2)**(1/2))
        return abs(self.y - other.y) + abs(self.x - other.y)


class Map:
    def __init__(self, grid: list[list[int]], start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.grid = grid

        self._max_y = len(self.grid)
        self._max_x = len(self.grid[0])
        self._step: tuple[Point, ...] = (Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0))

        self._display = [
            [chr(c + ord('a')) for c in y]
            for y in self.grid
        ]

    def display_points(self, points: list[Point]):
        display = deepcopy(self._display)
        for p in points:
            display[p.y][p.x] = '#'
        print('\n'+'\n'.join([''.join(y) for y in display]))

    def get_neighbors(self, point: Point):
        points: list[Point] = []
        for step in self._step:
            delta = point + step
            if delta.y > -1 and delta.y < self._max_y and delta.x > -1 and delta.x < self._max_x:
                points.append(delta)
        return points

    def get_height(self, point: Point) -> int:
        return self.grid[point.y][point.x]

    def a_star(self, two: bool = False) -> int:
        start = self.end if two else self.start
        end = self.end
        visited: list[Point] = []  # Our graph is not directed, so we need to keep track of already visited nodes
        came_from: dict[Point, Point] = {}  # To reconstruct the path once done
        g: dict[Point, int] = {start: 0}  # G Value for each node
        h: dict[Point, int] = {}
        to_consider: list[tuple[Point, float]] = [(start, g[start] + 0 if two else start.distance(self.end))]

        # i = 0
        while True:
            to_consider = sorted(to_consider, key=lambda x: x[1])
            current, f = to_consider.pop(0)

            current_height = self.get_height(current)
            if two:
                if current_height == 0:
                    end = current
                    break
            else:
                if current == end:
                    break

            visited.append(current)
            neighbours = self.get_neighbors(current)
            for neighbour in neighbours:
                delta = self.get_height(neighbour) - current_height
                invalid = delta < -1 if two else delta > 1
                if neighbour in visited or invalid:
                    continue
                tmp_g = g[current] + 1  # We only have simple 1 step costs in our graph
                if neighbour not in g or tmp_g < g[neighbour]:
                    came_from[neighbour] = current
                    g[neighbour] = tmp_g
                    if neighbour not in h:
                        h[neighbour] = 0 if two else neighbour.distance(self.end)
                    tmp_h = h[neighbour]
                    tmp_f = tmp_g + tmp_h
                    to_consider.append((neighbour, tmp_f))

        l: list[Point] = [end]
        while True:
            current = l[-1]
            if current not in came_from:
                self.display_points(l)
                return len(l) - 1
            prev = came_from[current]
            l.append(prev)

    @staticmethod
    def parse(data: str) -> 'Map':
        offset = ord('a')
        start: Point
        end: Point
        grid: list[list[int]] = []
        for y, line in enumerate(data.splitlines()):
            grid.append([])
            for x, char in enumerate(line):
                if char == 'S':
                    start = Point(y, x)
                    char = 'a'
                if char == 'E':
                    end = Point(y, x)
                    char = 'z'
                height = ord(char) - offset
                grid[y].append(height)
        return Map(grid, start, end)


# Running
m = Map.parse(data)
print(m.a_star(two=True))
