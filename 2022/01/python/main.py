#!/usr/bin/env python

from os.path import dirname, join

# Day 01

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


def count_calories(data: str, top_three=False) -> int:
    calories = [
        sum([int(calories) for calories in elve.split('\n')])
        for elve in data.split('\n\n')
    ]
    calories = sorted(calories, reverse=True)
    if not top_three:
        return calories[0]
    else:
        return sum(calories[0:3])


# 1
print('1.')
print(count_calories(test))
print(count_calories(data))

# 2
print('\n2.')
print('1.')
print(count_calories(test, True))
print(count_calories(data, True))
