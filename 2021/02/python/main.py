#!/usr/bin/env python

from os.path import join, dirname

# Day 01

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read()


# 1

class submarine:
    def __init__(self, with_aim=False):
        self.distance = 0
        self.depth = 0
        self.aim = 0
        self.with_aim = with_aim

    def execute(self, instruction: str):
        op, x = instruction.split(' ')
        x = int(x)
        if op == 'forward':
            if self.with_aim:
                self.distance += x
                self.depth += x * self.aim
            else:
                self.distance += x
        elif op == 'up':
            if self.with_aim:
                self.aim -= x
            else:
                self.depth -= x
        elif op == 'down':
            if self.with_aim:
                self.aim += x
            else:
                self.depth += x

    def execute_instructions(self, instructions: str):
        for instruction in instructions.strip().split('\n'):
            self.execute(instruction)

    def get_current_position(self):
        return self.distance * self.depth


test = read_input('test.txt')
sub = submarine()
sub.execute_instructions(test)
print(f"Test: {sub.get_current_position()}")

data = read_input('input.txt')
sub = submarine()
sub.execute_instructions(data)
print(f"Part 1: {sub.get_current_position()}")

# 2


sub = submarine(with_aim=True)
sub.execute_instructions(test)
print(f"Test: {sub.get_current_position()}")

sub = submarine(with_aim=True)
sub.execute_instructions(data)
print(f"Part 2: {sub.get_current_position()}")
