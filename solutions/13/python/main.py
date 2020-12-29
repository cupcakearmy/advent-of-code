from os.path import join, dirname
from typing import List, Tuple
from math import ceil, floor


class Station:

    def __init__(self, txt: str) -> None:
        arrival, busses = txt.strip().split('\n')
        self.arrival = int(arrival)
        self.busses = [
            int(bus)
            for bus in busses.replace('x', '0').split(',')
        ]

    @staticmethod
    def get_next_for_id(id: int, arrival: int) -> int:
        return id * ceil(arrival / id)

    def find_next(self) -> Tuple[int, int]:
        arrivals: List[Tuple[int, int]] = []
        for bus in self.busses:
            if bus == 0:
                continue
            arrivals.append((bus, self.get_next_for_id(bus, self.arrival)))
        return min(arrivals, key=lambda x: x[1])

    def get_flag(self) -> int:
        id, arrives = self.find_next()
        return id * (arrives - self.arrival)

    def contest(self, offset: int = 1) -> int:
        # Prepare
        highest = max(self.busses)
        highest_i = self.busses.index(highest)
        others = [
            (bus, i - highest_i)
            for i, bus in enumerate(self.busses)
            if bus != 0 and i != highest_i
        ]
        others.sort(key=lambda x: x[0], reverse=True)

        # Compute
        i: int = max(1, floor(offset / highest))
        while True:
            x = highest * i
            error = False
            for bus, diff in others:
                dx = x + diff
                if dx != self.get_next_for_id(bus, dx):
                    error = True
                    break
            if not error:
                return x - highest_i
            i += 1


data = join(dirname(__file__), '../data.txt')
with open(data) as f:

    # Some "testing"
    all = {
        '17,x,13,19': 3417,
        '67,7,59,61': 754018,
        '67,x,7,59,61': 779210,
        '67,7,x,59,61': 1261476,
        '1789,37,47,1889': 1202161486,
    }
    for busses, expected in all.items():
        station = Station('69\n' + busses)
        print(expected, expected == station.contest())

    txt = f.read()
    station = Station(txt)
    print(station.get_flag())
    print(station.contest(offset=10**14))
