#!/usr/bin/env python

from os.path import join, dirname

# Day 3

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# Running

Point = tuple[int, int]

class Line:
    def __init__(self, start:Point, end: Point) -> None:
        pass

class Wire:
    def __init__(self, points: list[Point]) -> None:
        self.points = points

    def __iter__(self):
        self.i = 0
        self.max = len(self.points) - 1
        return self

    def __next__(self):
        if self.i >= self.max:
            raise StopIteration
        value = (self.points[self.i], self.points[self.i +1])
        self.i += 1
        return value

    def __str__(self) -> str:
        return ', '.join([f'({x}, {y})' for x, y in self.points])

    def find_intersections(self, other: Line) -> list[Point]:
        matches: list[Point] = []
        for a in self:
            for b in other:
                if a[0][0] < b[0] 
                # if a[0] == b[0] and a[1] == b[1]:
                #     matches.append(a[0])
        return matches

    @staticmethod
    def parse(raw: str):
        commands = raw.split(',')
        current: Point = (0, 0)
        points: list[Point] = [current]
        for command in commands:
            direction = command[0]
            length = int(command[1:])
            match direction:
                case 'L':
                    current = (current[0] - length, current[1])
                case 'R':
                    current = (current[0] + length, current[1])
                case 'U':
                    current = (current[0], current[1] + length)
                case 'D':
                    current = (current[0], current[1] - length)
            points.append(current)
        return Wire(points)


class Panel():
    def __init__(self, wires: list[Wire]) -> None:
        self.wires = wires

    def find_closes(self):
        matches = self.wires[0].find_intersections(self.wires[1].line)
        distances = [abs(x)+abs(y) for x, y in matches]
        return min(distances)

    @staticmethod
    def parse(raw: str):
        return Panel(wires=[Wire.parse(line) for line in raw.splitlines()])


p = Panel.parse(test)
# print([str(w) for w in p.wires])
for wire in p.wires:
    print(wire)
    for line in wire:
        print(line)
# print(p.find_closes())
