#!/usr/bin/env python

import json
from dataclasses import dataclass
from functools import cmp_to_key
from os.path import dirname, join
from typing import Union

# Day 13

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')

Sequence = list[Union[int, 'Sequence']]


@dataclass
class Pair:
    left: Sequence
    right: Sequence

    @ staticmethod
    def parse(data: str) -> 'Pair':
        left, right = map(json.loads, data.splitlines())
        return Pair(left, right)


@ dataclass
class Transmission:
    pairs: list[Pair]

    def verify(self):
        total = 0
        for i, pair in enumerate(self.pairs):
            if Transmission._compare(pair.left, pair.right) > 0:
                total += i+1
        return total

    def sort(self) -> int:
        dividers: list[Sequence] = [[[2]], [[6]]]
        sequences: list[Sequence] = [*dividers]
        for pair in self.pairs:
            sequences += [pair.left, pair.right]
        sequences = sorted(sequences, key=cmp_to_key(Transmission._compare), reverse=True)
        decoder = 1
        for divider in dividers:
            decoder *= sequences.index(divider)+1
        return decoder

    @staticmethod
    def _compare(left: Sequence, right: Sequence) -> int:
        # print(f"Verifying {left} and {right}")
        type_left = type(left)
        type_right = type(right)
        if type_left != type_right:
            if type_left is int:
                left = [left]
            else:
                right = [right]
            return Transmission._compare(left, right)
        if type_left is int:
            return 0 if left == right else right - left
        if type_left is list:
            len_left = len(left)
            len_right = len(right)
            for i in range(min(len_left, len_right)):
                result = Transmission._compare(left[i], right[i])
                if result != 0:
                    return result
            return 0 if len_left == len_right else len_right - len_left
        return 0

    @ staticmethod
    def parse(data: str) -> 'Transmission':
        return Transmission([Pair.parse(pair) for pair in data.split('\n\n')])


# Running
transmission = Transmission.parse(data)
print(transmission.verify())
print(transmission.sort())
