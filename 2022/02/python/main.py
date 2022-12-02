#!/usr/bin/env python

from dataclasses import dataclass
from enum import Enum
from os.path import dirname, join

# Day 02

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


MAPPING = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,  # Rock of loose
    'Y': 2,  # Paper or draw
    'Z': 3,  # Scissor or win
}

# Bitwise precalculated
CASES = {
    1: (4, 3),
    2: (3, 5),
    3: (5, 4),
}


@dataclass
class Match:
    opponent: int
    you: int

    def score(self):
        # Draw is 3 points
        if self.opponent == self.you:
            return self.you + 3

        won = CASES[self.you][0] == self.you + self.opponent
        return self.you + (6 if won else 0)


@dataclass
class Game:
    matches: list[Match]

    def play(self):
        return sum([match.score() for match in self.matches])

    # Part 2
    def cheat(self):
        for match in self.matches:
            # Draw
            if match.you == 2:
                match.you = match.opponent
            else:
                win = 0 if match.you == 1 else 1
                match.you = CASES[match.opponent][win] - match.opponent

    @staticmethod
    def parse(data: str):
        lines = [line.split(' ') for line in data.split('\n')]
        matches = [Match(MAPPING[line[0]], MAPPING[line[1]]) for line in lines]
        return Game(matches)


# 1
print('1.')
game = Game.parse(test)
print(game.play())
game = Game.parse(data)
print(game.play())


# 2
print('\n2.')
game = Game.parse(test)
game.cheat()
print(game.play())
game = Game.parse(data)
game.cheat()
print(game.play())
