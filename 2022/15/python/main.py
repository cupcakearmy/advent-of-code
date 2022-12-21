#!/usr/bin/env python

import sys
from dataclasses import dataclass
from functools import lru_cache
from os.path import dirname, join
from typing import Union

# Day 15

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

    @lru_cache(maxsize=None)
    def manhattan(self, other: 'Point'):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def tuning_freq(self) -> int:
        return (self.x * 4000000) + self.y

    @staticmethod
    def parse(s: str) -> 'Point':
        return Point(*map(lambda s: int(s[2:]), s.split(', ')))  # Format: x=8, y=7


@dataclass
class Interval:
    start: int
    end: int

    def __contains__(self, other: Union[int, 'Interval']) -> bool:
        if type(other) is int:
            return self.start <= other and other <= self.end
        elif isinstance(other, Interval):
            return other.start in self or other.end in self
        return False

    def __add__(self, other: 'Interval') -> 'Interval':
        return Interval(min(self.start, other.start), max(self.end, other.end))

    def __len__(self) -> int:
        return abs(self.start - self.end) + 1

    @staticmethod
    def reduce(intervals: list['Interval']):
        combined: list['Interval'] = []
        for interval in intervals:
            for added in combined:
                if added in interval or interval in added:
                    combined.remove(added)
                    combined.append(added + interval)
                    break
            else:
                combined.append(interval)
        return combined if combined == intervals else Interval.reduce(combined)


@dataclass
class Map:
    sensors: dict[Point, Point]
    max_distance: int

    def analyse_line(self, line: int, minimum: int | float, maximum: int | float):
        intervals: list[Interval] = []
        for sensor, beacon in self.sensors.items():
            radius = sensor.manhattan(beacon)  # Radius of the sensor
            dy = radius - abs(sensor.y - line)  # Check if line is in the radius of the sensor
            if dy >= 0:
                # Add interval for scanned line
                intervals.append(Interval(max(minimum, sensor.x-dy), min(maximum, sensor.x+dy)))
        intervals = Interval.reduce(intervals)
        return sum([len(i) for i in intervals]), intervals

    def flag_1(self, line: int):
        score, _ = self.analyse_line(line, float('-inf'), float('inf'))
        return score - 1

    def flag_2(self, limit: int) -> int:
        for line in range(limit):
            score, intervals = self.analyse_line(line, 0, limit)
            if score != limit + 1:
                print(line, intervals)
                return Point(intervals[0].end + 1, line).tuning_freq()
        raise Exception("Not found")

    @ staticmethod
    def parse(data: str) -> 'Map':
        sensors: dict[Point, Point] = {}
        max_distance = 0
        for line in data.splitlines():
            sensor, beacon = line.split(':')
            s = Point.parse(sensor[10:])
            b = Point.parse(beacon[22:])
            sensors[s] = b
            max_distance = max(max_distance, s.manhattan(b))
        return Map(sensors, max_distance)


# Running

m = Map.parse(data)
print(m.flag_1(2000000))
print(Point(3446137, 3204480).tuning_freq())
# print(m.flag_2(4_000_000))
