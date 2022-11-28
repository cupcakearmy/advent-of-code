#!/usr/bin/env python

import math
from collections import defaultdict
from os.path import dirname, join

# Day 14

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Polymer:
    def __init__(self, state: str, insertions: dict[str, str]):
        self.state = state
        self.insertions = insertions
        self.states: defaultdict[str, int] = defaultdict(lambda: 0)

        for i in range(len(self) - 1):
            pair = self.state[i:i+2]
            self.states[pair] += 1

    def __len__(self):
        return len(self.state)

    def step(self):
        new = defaultdict(lambda: 0)
        for state, count in self.states.items():
            if count == 0:
                continue
            insertion = self.insertions[state]
            for key in [state[0] + insertion, insertion + state[1]]:
                new[key] += count
        self.states = new

    def score(self):
        elements = defaultdict(lambda: 0)
        for state, count in self.states.items():
            for element in state:
                elements[element] += count
        for element, count in elements.items():
            elements[element] = math.ceil(elements[element]/2)
        return max(elements.values()) - min(elements.values())

    def flag(self, steps: int):
        for _ in range(steps):
            self.step()
        print(self.score())

    @staticmethod
    def parse(data: str):
        state, raw = data.split('\n\n')
        lines = [
            l.split(' -> ')
            for l in raw.split('\n')
        ]
        insertions = {
            i[0]: i[1]
            for i in lines
        }
        return Polymer(state.strip(), insertions)


# 1
print('1.')

polymer = Polymer.parse(test)
polymer.flag(10)
polymer = Polymer.parse(data)
polymer.flag(10)

# 2
print('\n2.')
polymer = Polymer.parse(test)
polymer.flag(40)
polymer = Polymer.parse(data)
polymer.flag(40)
