#!/usr/bin/env python

from os.path import join, dirname
from typing import overload
from copy import deepcopy

# Day 2

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# Running


class Interpreter:
    def __init__(self, memory: list[int]) -> None:
        self.initial = memory
        self.reset()

    def reset(self):
        self.counter = 0
        self.halt = False
        self.memory = deepcopy(self.initial)

    @overload
    def pointer(self, offset: int, value:  int) -> None: ...
    @overload
    def pointer(self, offset: int, value:  None = None) -> int: ...

    def pointer(self, offset: int, value: int | None = None) -> int | None:
        p = self.memory[self.counter+offset]
        if value:
            self.memory[p] = value
        return self.memory[p]

    def operation(self):
        size = 0
        match self.memory[self.counter]:
            case 1:
                left = self.pointer(1)
                right = self.pointer(2)
                self.pointer(3, left + right)
                size = 3
            case 2:
                left = self.pointer(1)
                right = self.pointer(2)
                self.pointer(3, left * right)
                size = 3
            case 99:
                self.halt = True
        self.counter += 1 + size

    def run(self):
        while not self.halt:
            self.operation()

    def restore(self):
        self.memory[1] = 12
        self.memory[2] = 2

    def __str__(self) -> str:
        return ", ".join(map(str, self.memory))


def find(i: Interpreter, target: int):
    for noun in range(0, 100):
        for verb in range(0, 100):
            i.reset()
            i.memory[1] = noun
            i.memory[2] = verb
            i.run()
            if i.memory[0] == target:
                return 100 * noun + verb


# Part 1
i = Interpreter(list(map(int, data.split(','))))
i.restore()
i.run()
print(i.memory[0])

# Part 2
print(find(i, 19690720))
