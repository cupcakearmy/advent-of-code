#!/usr/bin/env python

from dataclasses import dataclass, field
from enum import Enum
from os.path import dirname, join

# Day 10

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# 1
print('1.')


class ResultType(Enum):
    Valid = 1
    Incomplete = 2
    Corrupted = 3


def empty_list() -> list[str]:
    return []


@dataclass
class ParseResult:
    type: ResultType = ResultType.Valid
    stack: list[str] = field(default_factory=empty_list)
    expected: str = ''
    found: str = ''


class NavigationSubsystemLineParser():
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    def __init__(self, line: str):
        self.line = line
        self.stack: list[str] = []
        self.position = 0

    def _allowed_chars(self):
        allowed = list(self.pairs.keys())
        if len(self.stack):
            value = self.stack[-1]
            if value in self.pairs:
                allowed.append(self.pairs[value])
        return allowed

    def validate(self) -> ParseResult:
        """
        Returns -1 for incomplete, 0 for valid, or the position of the first invalid character
        """
        while self.position < len(self.line):
            expected = self._allowed_chars()
            char = self.line[self.position]
            is_opening = char in self.pairs
            if is_opening:
                self.stack.append(char)
            else:
                expected = self.pairs[self.stack[-1]]
                if char != expected:
                    return ParseResult(ResultType.Corrupted, expected=expected, found=char)
                else:
                    self.stack.pop()

            self.position += 1
        incomplete = len(self.stack) > 0
        return ParseResult(type=ResultType.Incomplete if incomplete else ResultType.Valid, stack=self.stack)


class NavigationSubsystem():

    def __init__(self, data: list[str]):
        self.data = data

    def validate(self) -> list[ParseResult]:
        return [NavigationSubsystemLineParser(line).validate() for line in self.data]

    def count_corrupted(self) -> int:
        results = self.validate()
        points_map = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        points = [points_map[result.found] for result in results if result.type == ResultType.Corrupted]
        return sum(points)

    def _calculate_autocomplete_score(self, stack: list[str]) -> int:
        points_map = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4
        }
        stack.reverse()
        total = 0
        for char in stack:
            total *= 5
            total += points_map[char]
        return total

    def autocomplete(self) -> int:
        results = [NavigationSubsystemLineParser(line).validate() for line in self.data]
        points = [
            self._calculate_autocomplete_score(result.stack)
            for result
            in results
            if result.type == ResultType.Incomplete
        ]
        points.sort()
        return points[len(points)//2]

    @staticmethod
    def parse(data: str):
        return NavigationSubsystem(data.splitlines())


parser = NavigationSubsystem.parse(test)
points = parser.count_corrupted()
print(points)

parser = NavigationSubsystem.parse(data)
points = parser.count_corrupted()
print(points)

# 2
print('\n2.')

parser = NavigationSubsystem.parse(test)
points = parser.autocomplete()
print(points)

parser = NavigationSubsystem.parse(data)
points = parser.autocomplete()
print(points)
