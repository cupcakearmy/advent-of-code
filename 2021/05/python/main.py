#!/usr/bin/env python

from os.path import join, dirname
from typing import List

# Day 05

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    @staticmethod
    def parse(raw: str):
        x, y = raw.strip().split(',')
        return Point(int(x), int(y))


class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def is_straight(self) -> bool:
        return self.a.x == self.b.x or self.a.y == self.b.y

    def is_diagonal(self) -> bool:
        return abs(self.a.x - self.b.x) == abs(self.a.y - self.b.y)

    def get_points(self) -> List[Point]:
        if self.is_straight():
            if self.a.x == self.b.x:
                return [
                    Point(self.a.x, y) for y
                    in range(min(self.a.y, self.b.y), max(self.a.y, self.b.y) + 1)
                ]
            else:
                return [
                    Point(x, self.a.y) for x
                    in range(min(self.a.x, self.b.x), max(self.a.x, self.b.x) + 1)
                ]
        else:
            dx = self.a.x - self.b.x
            dy = self.a.y - self.b.y
            sign_x = 1 if dx < 0 else -1
            sign_y = 1 if dy < 0 else -1
            return [
                Point(self.a.x + sign_x * i, self.a.y + sign_y * i)
                for i in range(abs(dx) + 1)
            ]

    def __repr__(self) -> str:
        return f'{self.a} → {self.b}'

    @staticmethod
    def parse(raw: str):
        a, b = raw.strip().split('->')
        return Line(Point.parse(a), Point.parse(b))


class Scan:
    def __init__(self, lines: List[Line]):
        self.lines = lines

    def keep_straight(self):
        self.lines = [line for line in self.lines if line.is_straight()]

    def keep_straight_and_diagonal(self):
        self.lines = [
            line for line in self.lines
            if line.is_straight() or line.is_diagonal()
        ]

    def matrix(self) -> List[List[int]]:
        x_max = max(max(line.a.x, line.b.x) for line in self.lines)
        y_max = max(max(line.a.y, line.b.y) for line in self.lines)
        matrix = [
            [0 for _ in range(x_max + 1)]
            for _ in range(y_max + 1)
        ]
        for line in self.lines:
            for point in line.get_points():
                matrix[point.y][point.x] += 1
        return matrix

    def plot(self) -> str:
        output = '\n'.join([
            ' '.join(str(x) for x in row)
            for row in self.matrix()
        ])
        return output.replace('0', '.')

    def danger(self) -> int:
        matrix = self.matrix()
        return sum(
            sum(1 for x in row if x > 1)
            for row in matrix
        )

    @ staticmethod
    def parse(raw: str):
        return Scan([Line.parse(line) for line in raw.strip().split('\n')])


test = read_input('test.txt')
data = read_input('input.txt')

# 1
print('1.')
scan = Scan.parse(test)
scan.keep_straight()
print(scan.plot())
print('Test: ', scan.danger())

scan = Scan.parse(data)
scan.keep_straight()
print('Real: ', scan.danger())

# 2
print('\n2.')

scan = Scan.parse(test)
scan.keep_straight_and_diagonal()
print(scan.plot())
print('Test: ', scan.danger())

scan = Scan.parse(data)
scan.keep_straight_and_diagonal()
print('Real: ', scan.danger())
