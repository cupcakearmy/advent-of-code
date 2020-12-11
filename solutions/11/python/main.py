from os.path import join, dirname
from typing import List, Optional
from itertools import product
from copy import deepcopy

TSeats = List[List[Optional[bool]]]

mapping = {
    '.': None,
    '#': True,
    'L': False
}
inv = {v: k for k, v in mapping.items()}


class Seats:
    p = [-1, 0, 1]

    def __init__(self, plan: str, alt: bool = False) -> None:
        self.seats: TSeats = [
            [
                mapping[seat]
                for seat in row
            ]
            for row in plan.strip().split('\n')
        ]
        self.max_x = len(self.seats[0])
        self.max_y = len(self.seats)
        self.alt = alt

    def __str__(self) -> str:
        return '\n'.join([
            ''.join([inv[seat] for seat in row])
            for row in self.seats
        ])

    def find_next_in_direction(self, y: int, x: int, dy: int, dx: int) -> Optional[bool]:
        y += dy
        x += dx
        while 0 <= x < self.max_x and 0 <= y < self.max_y:
            cur = self.seats[y][x]
            if cur is not None:
                return cur
            y += dy
            x += dx
        return None

    def get_occupied(self, y: int, x: int,) -> int:
        occupied = 0
        for dx, dy in product(self.p, self.p):
            if dx == 0 and dy == 0:
                continue
            if self.alt and self.find_next_in_direction(y, x, dy, dx) == True:
                occupied += 1
            else:
                dx += x
                dy += y
                if 0 <= dx < self.max_x and 0 <= dy < self.max_y and self.seats[dy][dx]:
                    occupied += 1
        return occupied

    def iteration(self) -> int:
        changed = 0
        future: TSeats = deepcopy(self.seats)
        required_to_leave = 4 if self.alt else 3
        for y, x in product(range(self.max_y), range(self.max_x)):
            current = self.seats[y][x]
            if current == None:
                continue
            occupied = self.get_occupied(y, x)
            if (current == True and occupied > required_to_leave) or (current == False and occupied == 0):
                future[y][x] = not current
                changed += 1
        self.seats = future
        return changed

    def count_occupied(self) -> int:
        return sum([
            sum([
                1 if seat == True else 0
                for seat in row
            ])
            for row in self.seats
        ])

    def find_equilibrium(self) -> int:
        while self.iteration() > 0:
            pass
        return self.count_occupied()


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    txt = f.read()
    seats = Seats(txt)
    print(seats.find_equilibrium())

    seats = Seats(txt, True)
    print(seats.find_equilibrium())
