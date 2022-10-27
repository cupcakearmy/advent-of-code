#!/usr/bin/env python

from os.path import join, dirname
from typing import List

# Day 09

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


def make_string_blue(string):
    return f'\033[94m{string}\033[0m'


def make_string_red(string):
    return f'\033[91m{string}\033[0m'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return False
        return self.x == o.x and self.y == o.y

    def value(self, data: List[List[int]]):
        return data[self.y][self.x]


class Floor:
    def __init__(self, data: List[List[int]]):
        self.data = data
        self.max_x = len(data[0])
        self.max_y = len(data)

    def paint(self, blue: List[Point] = [], red: List[Point] = []) -> str:
        out = ''
        for y in range(self.max_y):
            for x in range(self.max_x):
                v = str(self.data[y][x])
                if Point(x, y) in red:
                    v = f'\033[31m{v}\033[0m'
                elif Point(x, y) in blue:
                    v = f'\033[34m{v}\033[0m'
                out += v
            out += '\n'
        return out

    def get_neighbors(self, point: Point) -> List[Point]:
        neighbors = []
        if point.x - 1 >= 0:
            neighbors.append(Point(point.x - 1, point.y))
        if point.x + 1 < self.max_x:
            neighbors.append(Point(point.x + 1, point.y))
        if point.y - 1 >= 0:
            neighbors.append(Point(point.x, point.y - 1))
        if point.y + 1 < self.max_y:
            neighbors.append(Point(point.x, point.y + 1))
        return neighbors

    def find_lowest_points(self) -> List[Point]:
        lowest_points = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                p = Point(x, y)
                neighbors = self.get_neighbors(p)
                values = [p.value(self.data) for p in neighbors]
                if p.value(self.data) < min(values):
                    lowest_points.append(p)
        return lowest_points

    def find_basins(self):
        lowest = self.find_lowest_points()
        basins = []
        for point in lowest:
            basin = set([point])
            edges = set([point])
            while len(edges) > 0:
                new_edges = set()
                for edge in edges:
                    neighbors = self.get_neighbors(edge)
                    for neighbor in neighbors:
                        if neighbor not in basin and neighbor.value(self.data) < 9:
                            basin.add(neighbor)
                            new_edges.add(neighbor)
                edges = new_edges
            basins.append(basin)
        print(self.paint(
            [point for basin in basins for point in basin], lowest))
        return basins

    def flag2(self) -> int:
        basins = self.find_basins()
        sizes = [len(b) for b in basins]
        sizes = sorted(sizes, reverse=True)
        total = 1
        for size in sizes[0:3]:
            total *= size
        return total

    def flag(self) -> int:
        points = self.find_lowest_points()
        return sum([
            p.value(self.data) + 1
            for p in points
        ])

    @staticmethod
    def parse(data: str):
        return Floor([
            list(map(int, list(row)))
            for row in data.split('\n')
        ])


# 1
print('1.')

floor = Floor.parse(test)
print(floor.paint(floor.find_lowest_points()))
print(f'Test: {floor.flag()}')

floor = Floor.parse(data)
print(floor.paint(floor.find_lowest_points()))
print(f'Real: {floor.flag()}')

# 2
print('\n2.')

floor = Floor.parse(test)
print(f'Test: {floor.flag2()}')

floor = Floor.parse(data)
print(f'Real: {floor.flag2()}')
