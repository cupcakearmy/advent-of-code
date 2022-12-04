#!/usr/bin/env python

from os.path import dirname, join

# Day 03

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


def score(char: str) -> int:
    offset = 97-1 if char.islower() else 65-27
    return ord(char) - offset


class Rucksack:
    def __init__(self, items: str):
        self.l = len(items) // 2
        self.items = items

    def find_common(self) -> str:
        front = self.items[:self.l]
        back = self.items[self.l:]
        intersection = set(front).intersection(set(back))
        return list(intersection)[0]


class Supplies:
    def __init__(self, rucksacks: list[Rucksack]) -> None:
        self.rucksacks = rucksacks

    def get_common(self):
        return sum([
            score(rucksack.find_common())
            for rucksack in self.rucksacks
        ])

    def groups(self):
        group_size = 3
        total = 0
        for i in range(len(self.rucksacks)//group_size):
            i *= group_size
            subset = self.rucksacks[i:i+group_size]
            sets = [set(rucksack.items) for rucksack in subset]
            chars = sets[0]
            for s in sets[1:]:
                chars = chars.intersection(s)
            total += score(list(chars)[0])
        return total

    @staticmethod
    def parse(data: str):
        rucksacks = [
            Rucksack(item)
            for item in data.split('\n')
        ]
        return Supplies(rucksacks)


# 1
print('1.')
supplies = Supplies.parse(test)
print(supplies.get_common())
supplies = Supplies.parse(data)
print(supplies.get_common())


# 2
print('\n2.')
supplies = Supplies.parse(test)
print(supplies.groups())
supplies = Supplies.parse(data)
print(supplies.groups())
