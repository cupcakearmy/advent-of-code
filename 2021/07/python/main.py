#!/usr/bin/env python

from os.path import join, dirname

# Day 07

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# 1


def get_cheapest_alignment(raw: str) -> int:
    crabs = [int(x) for x in raw.split(',')]
    median = sorted(crabs)[len(crabs) // 2]
    costs = [abs(x - median) for x in crabs]
    return sum(costs)


print('1.')
result = get_cheapest_alignment(test)
print(result)
result = get_cheapest_alignment(data)
print(result)

# 2


def triangle_number(distance: int) -> int:
    return distance * (distance + 1) // 2


def get_cheapest_alignment_complex(raw: str) -> int:
    crabs = [int(x) for x in raw.split(',')]
    lower = min(crabs)
    upper = max(crabs)
    lowest = -1
    for target in range(lower, upper + 1):
        cost = sum([triangle_number(abs(x - target)) for x in crabs])
        if lowest == -1 or cost < lowest:
            lowest = cost
    return lowest


print('2.')
result = get_cheapest_alignment_complex(test)
print(result)
result = get_cheapest_alignment_complex(data)
print(result)
