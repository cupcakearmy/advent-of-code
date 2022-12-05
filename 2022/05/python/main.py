#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join

# Day 05

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().rstrip()


test = read_input('test.txt')
data = read_input('input.txt')


def clean(s: str, words: list[str], strip=True) -> str:
    for word in words:
        s = s.replace(word, '')
    return s.strip() if strip else s


@dataclass
class Operation:
    amount: int
    start: int
    end: int


@dataclass
class Crane:
    stacks: list[list[str]]
    operations: list[Operation]

    def operate(self, crate_mover_9001=False):
        for operation in self.operations:
            items = self.stacks[operation.start][-operation.amount:]
            self.stacks[operation.end] += items if crate_mover_9001 else reversed(items)
            self.stacks[operation.start] = self.stacks[operation.start][:-operation.amount]

    def flag(self):
        msg = ''
        for stack in self.stacks:
            msg += stack[-1]
        return msg

    @staticmethod
    def parse(data: str):
        stacks_raw, operations_raw = data.split('\n\n')
        operations = [
            Operation(*map(int, clean(operation, ['move ', 'from ', 'to ']).split(' ')))
            for operation in operations_raw.split('\n')
        ]
        for operation in operations:
            operation.start -= 1
            operation.end -= 1
        stack_lines = stacks_raw.split('\n')
        stacks_size = len(clean(stack_lines[-1], ['  ']).split(' '))
        stacks: list[list[str]] = [[] for _ in range(stacks_size)]
        for line in reversed(stack_lines[:-1]):
            for i in range(stacks_size):
                item = line[i*4 + 1]
                if item != ' ':
                    stacks[i].append(item)
        return Crane(stacks, operations)


# 1
print('1.')
crane = Crane.parse(test)
crane.operate()
print(crane.flag())

crane = Crane.parse(data)
crane.operate()
print(crane.flag())

# 2
print('\n2.')
crane = Crane.parse(test)
crane.operate(crate_mover_9001=True)
print(crane.flag())

crane = Crane.parse(data)
crane.operate(crate_mover_9001=True)
print(crane.flag())
