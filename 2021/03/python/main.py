#!/usr/bin/env python

from os import O_EXCL
from os.path import join, dirname
from typing import Tuple

# Day 03

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# 1


def count_bits(input: str) -> Tuple[int, int]:
    gamma = 0
    epsilon = 0
    lines = input.split('\n')
    size = len(lines[0])
    for x in range(size):
        zeros = 0
        ones = 0
        for line in lines:
            if line[x] == '0':
                zeros += 1
            else:
                ones += 1
        incr = 2**(size - x - 1)
        if zeros < ones:
            gamma += incr
        else:
            epsilon += incr
    return gamma, epsilon


print('1.')
gamma, epsilon = count_bits(test)
print(
    f"Test: Gamma: {gamma}, Epsilon: {epsilon}, Power Consumption: {gamma * epsilon}")
gamma, epsilon = count_bits(data)
print(
    f"Data: Gamma: {gamma}, Epsilon: {epsilon}, Power Consumption: {gamma * epsilon}")
# 2


def extract(input: str, bigger=True) -> int:
    lines = input.split('\n')
    size = len(lines[0])
    for x in range(size):
        zeros = 0
        ones = 0
        for line in lines:
            if line[x] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros == ones:
            filter = '1' if bigger else '0'
        elif bigger:
            filter = '0' if zeros > ones else '1'
        else:
            filter = '0' if zeros < ones else '1'
        lines = [
            line for line in lines
            if line[x] == filter
        ]
        if len(lines) == 1:
            return int(lines[0], 2)
    raise Exception('No solution found')


print('\n2.')
oxygen = extract(test, True)
co2 = extract(test, False)
life_support = oxygen * co2
print(f"Test: Oxygen: {oxygen}, CO2: {co2}, Life Support: {life_support}")

oxygen = extract(data, True)
co2 = extract(data, False)
life_support = oxygen * co2
print(f"Data: Oxygen: {oxygen}, CO2: {co2}, Life Support: {life_support}")
