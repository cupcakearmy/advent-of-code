#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join

# Day 04

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass
class CleaningJob:
    start: int
    end: int

    def __len__(self):
        return self.end - self.start

    def __contains__(self, other) -> bool:
        if isinstance(other, CleaningJob):
            return self.start <= other.start and self.end >= other.end
        elif type(other) is int:
            return self.start <= other <= self.end
        else:
            return False

    def overlaps(self, other: 'CleaningJob') -> bool:
        return other.start in self or other.end in self or other in self


@dataclass
class CleaningPair:
    one: CleaningJob
    two: CleaningJob

    @staticmethod
    def parse(data: str):
        jobs = [
            CleaningJob(*map(int, job.split('-')))
            for job in data.split(',')
        ]
        return CleaningPair(*jobs)

    def is_duplicated(self):
        return self.one in self.two or self.two in self.one

    def overlaps(self):
        return self.one.overlaps(self.two) or self.two.overlaps(self.one)


@dataclass
class CleaningSquad:
    pairs: list[CleaningPair]

    @staticmethod
    def parse(data: str):
        return CleaningSquad([
            CleaningPair.parse(line)
            for line in data.split('\n')
        ])

    def check_duplicate(self):
        return sum([pair.is_duplicated() for pair in self.pairs])

    def check_overlap(self):
        return sum([pair.overlaps() for pair in self.pairs])

        # 1
print('1.')
squad = CleaningSquad.parse(test)
print(squad.check_duplicate())
squad = CleaningSquad.parse(data)
print(squad.check_duplicate())

# 2
print('\n2.')
squad = CleaningSquad.parse(test)
print(squad.check_overlap())
squad = CleaningSquad.parse(data)
print(squad.check_overlap())
