#!/usr/bin/env python

from functools import reduce
from os.path import dirname, join
from typing import Literal

# Day 11

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

Old = Literal['old']
Operator = Literal['+', '*']
Operation = tuple[Operator, Old | int]


class Monkey:
    def __init__(self, items: list[int], operation: Operation, test: tuple[int, int, int], chill: bool) -> None:
        self.items = items
        self.chill = chill
        self.inspected: int = 0

        self.divisible = test[0]
        self.true = test[1]
        self.false = test[2]

        op, arg = operation
        self._old = arg == 'old'
        self._add = op == '+'
        self._arg = -1 if self._old else int(arg)

    def round(self) -> list[tuple[int, int]]:
        l: list[tuple[int, int]] = []
        for value in self.items:
            arg = value if self._old else self._arg
            value = value + arg if self._add else value * arg
            if self.chill:
                value = value // 3
            next_monkey = self.true if value % self.divisible == 0 else self.false
            l.append((next_monkey, value))
        self.inspected += len(self.items)
        self.items.clear()
        return l

    def __repr__(self) -> str:
        return f"{self.inspected}"

    @staticmethod
    def parse(data: str, chill: bool):
        lines = data.splitlines()
        items = list(map(int, lines[1][18:].split(', ')))
        # Operator
        op_raw, arg_raw = lines[2][22:].split()
        op: Operator = op_raw
        arg: Old | int = 'old' if arg_raw == 'old' else int(arg_raw)
        operation: Operation = (op, arg)
        # Test
        divisible = int(lines[3][21:])
        true = int(lines[4][29:])
        false = int(lines[5][30:])
        return Monkey(items, operation, (divisible, true, false), chill)


class Game:
    def __init__(self, monkeys: list[Monkey]) -> None:
        self.monkeys = monkeys
        dividers = [m.divisible for m in monkeys]
        self.common = reduce(lambda a, b: a*b, dividers, 1)

    def __str__(self) -> str:
        return ", ".join(map(str, self.monkeys))

    def round(self):
        for monkey in self.monkeys:
            thrown = monkey.round()
            for monkey, item in thrown:
                self.monkeys[monkey].items.append(item % self.common)

    def flag(self, rounds: int = 20):
        for _ in range(rounds):
            self.round()
        inspected = [monkey.inspected for monkey in self.monkeys]
        inspected = (sorted(inspected)[-2:])
        return inspected[0] * inspected[1]

    @staticmethod
    def parse(data: str, chill: bool = True):
        return Game([Monkey.parse(monkey, chill) for monkey in data.split('\n\n')])


# Running
game = Game.parse(data, chill=True)
print(game.flag(20))

game = Game.parse(data, chill=False)
print(game.flag(10_000))
