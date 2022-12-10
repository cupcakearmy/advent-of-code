#!/usr/bin/env python

from os.path import dirname, join
from typing import Literal, Union

# Day 10

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

Instruction = tuple[int, Union[
    tuple[Literal['noop']],
    tuple[Literal['addx'], int]
]]


class CRT:
    def __init__(self) -> None:
        self.clock = 0
        self.display = [
            ['.' for _ in range(40)]
            for _ in range(6)
        ]

    def step(self, position: int):
        sprite = self.clock % 40
        if position - 1 <= sprite and sprite <= position+1:
            y = self.clock // 40
            x = sprite
            self.display[y][x] = "#"
        self.clock += 1

    def __str__(self) -> str:
        return '\n'.join(map(lambda line: ''.join(line), self.display))


class CPU:
    def __init__(self, instructions: list[Instruction]) -> None:
        self.instructions = instructions
        self.cycle = 1
        self.register = 1
        self.processing: Instruction = self.instructions.pop(0)
        self.crt = CRT()

    def step(self) -> bool:
        self.cycle += 1
        count, instruction = self.processing
        if count > 1:
            self.processing = (count-1, instruction)
        else:
            match instruction[0]:
                case 'noop':
                    pass
                case 'addx':
                    self.register += instruction[1]
            if len(self.instructions) == 0:
                return True
            self.processing = self.instructions.pop(0)
        return False

    def signal_strength(self):
        return self.cycle * self.register

    def run(self):
        signals = 0
        while True:
            self.crt.step(self.register)
            halted = self.step()
            if (self.cycle + 20) % 40 == 0:
                signals += self.signal_strength()
            if halted:
                break
        return signals

    def __str__(self) -> str:
        return f"{self.cycle} X={self.register} {self.processing} SS={self.signal_strength()}\n{self.crt}"

    @staticmethod
    def parse(data: str):
        instructions: list[Instruction] = []
        for line in data.splitlines():
            command, *args = line.split()
            match command:
                case 'noop':
                    instructions.append((1, (command, )))
                case 'addx':
                    instructions.append((2, (command, int(args[0]))))
        return CPU(instructions)


# Running
cpu = CPU.parse(test)
print(cpu.run())
print(cpu)

cpu = CPU.parse(data)
print(cpu.run())
print(cpu)
