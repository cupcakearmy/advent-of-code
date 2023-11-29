---
to: <%= dir %>/python/main.py
unless_exists: true
---
#!/usr/bin/env python

from os.path import join, dirname

# Setup


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


TEST = read_input('test.txt')
INPUT = read_input('input.txt')

# Task

def part_a(raw: str):
    pass


def part_b(raw: str):
    pass

# Running

print('1.')
print(part_a(TEST))
print(part_a(INPUT))

print('\n2.')
print('1.')
print(part_b(TEST))
print(part_b(INPUT))
