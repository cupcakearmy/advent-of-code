#!/usr/bin/env python

from os.path import join, dirname
from typing import Dict, List

# Day 06

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class School:
    def __init__(self, fishes: List[int]) -> None:
        self.fishes = [0] * 9
        for fish in fishes:
            self.fishes[fish] += 1

    @staticmethod
    def parse(raw: str):
        return School([int(x) for x in raw.split(',')])

    def __len__(self) -> int:
        return sum(self.fishes)

    def tick(self):
        born, *rest = self.fishes.copy()
        self.fishes = rest + [born]
        self.fishes[6] += born

    def simulate(self, days: int):
        for _ in range(days):
            self.tick()


# 1
print('1.')

school = School.parse(test)
school.simulate(18)
print(len(school))
school.simulate(80)
print(f'Test: {len(school)}')

school = School.parse(data)
school.simulate(80)
print(f'Data: {len(school)}')

# 2
print('\n2.')

school = School.parse(test)
school.simulate(256)
print(f'Test: {len(school)}')

school = School.parse(data)
school.simulate(256)
print(f'Data: {len(school)}')
