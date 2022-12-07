#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join

# Day 06

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


def find_marker(buffer, size=4) -> int:
    for i in range(len(buffer)):
        subset = buffer[i:i+size]
        if len(subset) == len(set(subset)):
            return i + size
    return -1


# 1
print('1.')
print(find_marker(test))
print(find_marker(data))

# 2
print('\n2.')
print(find_marker(test, size=14))
print(find_marker(data, size=14))
