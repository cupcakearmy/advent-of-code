#!/usr/bin/env python

from os.path import join, dirname
from typing import Dict, List, Set

# Day 08

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Utils:
    @staticmethod
    def count_chars(items: List[str]) -> Dict[str, int]:
        count = {}
        for item in items:
            for char in item:
                if char not in count:
                    count[char] = 0
                count[char] += 1
        return count

    @staticmethod
    def group_by_length(items: List[str]) -> Dict[int, List[str]]:
        groups = {}
        for item in items:
            l = len(item)
            if l not in groups:
                groups[l] = []
            groups[l].append(item)
        return groups


class SevenSegment:
    mappings = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }
    reverse = {v: k for k, v in mappings.items()}
    count: Dict[str, int] = Utils.count_chars(mappings.values())

    @staticmethod
    def encode(number: int) -> str:
        return SevenSegment.mappings[number]

    @staticmethod
    def decode(segment: str) -> int:
        normalized: str = ''.join(sorted(list(segment)))
        return SevenSegment.reverse[normalized]


class Reading:
    def __init__(self, input: List[str], output: List[str]) -> None:
        self.input = input
        self.output = output
        self.transformations: Dict[str, str] = {}

    def translate(self, segment: str) -> str:
        return ''.join([self.transformations[char] for char in segment])

    def analyse(self):
        count = Utils.count_chars(self.input)
        by_length = Utils.group_by_length(self.input)

        # Find a & c
        # 1 and 7 have the same chars with the only difference of the 'a'
        one = set(by_length[2][0])
        seven = set(by_length[3][0])
        a = seven.difference(one).pop()

        dg: Set[str] = set()

        # Find b, e & f by statistical analysis
        for k, v in count.items():
            if v == 6:
                b = k
                self.transformations[k] = 'b'
            elif v == 4:
                self.transformations[k] = 'e'
            elif v == 9:
                self.transformations[k] = 'f'
            elif v == 8:
                if k == a:
                    self.transformations[k] = 'a'
                else:
                    self.transformations[k] = 'c'
            elif v == 7:
                dg.add(k)

        # Find d by looking at the 1 and 4
        # We already know b so, we subtract cf (1) from bcdf (4) and are left with bd.
        four = set(by_length[4][0])
        bd = four.difference(one)
        d = bd.difference(b).pop()
        self.transformations[d] = 'd'
        g = dg.difference(d).pop()
        self.transformations[g] = 'g'

    def read(self) -> List[int]:
        return [SevenSegment.decode(self.translate(segment)) for segment in self.output]

    @staticmethod
    def parse(data: str):
        input, output = data.split('|')
        i = input.strip().split(' ')
        o = output.strip().split(' ')
        return Reading(i, o)


class Log:
    def __init__(self, readings: List[Reading]) -> None:
        self.readings = readings

    def flag(self, alt=False):
        count = 0
        for reading in self.readings:
            reading.analyse()
            numbers = reading.read()
            if alt:
                count += int(''.join([str(n) for n in numbers]))
            else:
                for number in numbers:
                    if number == 1 or number == 4 or number == 7 or number == 8:
                        count += 1
        return count

    @staticmethod
    def parse(data: str):
        return Log([Reading.parse(line) for line in data.split('\n')])


# 1
print('1.')

log = Log.parse(test)
result = log.flag()
print(f"Test: {result}")

log = Log.parse(data)
result = log.flag()
print(f"Result: {result}")

# 2
print('\n2.')

log = Log.parse(test)
result = log.flag(True)
print(f"Test: {result}")

log = Log.parse(data)
result = log.flag(True)
print(f"Result: {result}")
