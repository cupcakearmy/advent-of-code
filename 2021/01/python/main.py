#!/usr/bin/env python

from os.path import join, dirname
from typing import List

# Day 01

# Common


def read_input(filename) -> str:
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read()


def parse(raw):
    return [int(x) for x in raw.strip().split('\n')]


test = parse(read_input('test.txt'))
test2 = parse(read_input('test_2.txt'))
data = parse(read_input('input.txt'))

# 1


def count_increasing(data: List[int]) -> int:
    total = 0
    for x in range(1, len(data)):
        if data[x] > data[x - 1]:
            total += 1
    return total


print('1. ')
print(f"Test: {count_increasing(test)}")
print(f"Result: {count_increasing(data)}")

# 2


def data_to_windows(data: List, size: int) -> List:
    windows = []
    for x in range(0, len(data) - size + 1):
        windows.append(sum(data[x:x + size]))
    return windows


print('2.')
print(f"Test: {count_increasing(data_to_windows(test2, 3))}")
print(f"Result: {count_increasing(data_to_windows(data, 3))}")
