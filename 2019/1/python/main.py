#!/usr/bin/env python

from os.path import join, dirname

# Day 1

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

# Running

# Part 1


def get_fuel_by_mass(mass: int):
    return mass // 3 - 2


total = sum([get_fuel_by_mass(int(x)) for x in data.splitlines()])
print(total)


# Part 2

def get_fuel_by_mass_rec(mass: int):
    if mass <= 6:
        return 0
    fuel = get_fuel_by_mass(mass)
    return fuel + get_fuel_by_mass_rec(fuel)


total = sum([get_fuel_by_mass_rec(int(x)) for x in data.splitlines()])
print(total)
