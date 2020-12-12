from os.path import join, dirname
from typing import List, Optional
from math import cos, sin, radians, atan2, degrees, sqrt

directions = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}


class Ship:

    def __init__(self, waypoint=False) -> None:
        self.x: float = 0
        self.y: float = 0
        self.d: int = directions['E']

        self.waypoint = waypoint
        self.wx: float = 10
        self.wy: float = 1

    @property
    def distance(self) -> int:
        return round(abs(self.x) + abs(self.y))

    def __str__(self) -> str:
        return f'⛴  X={round(self.x)} Y={round(self.y)} 𒎓={round(self.d)}\t🏴‍☠️ X={round(self.wx)} Y={round(self.wy)}'

    def navigate(self,  amount: int, degree: Optional[int] = None) -> None:
        if degree == None:
            if self.waypoint:
                self.x += self.wx * amount
                self.y += self.wy * amount
                return
            degree = self.d
        dx = amount * sin(radians(degree))
        dy = amount * cos(radians(degree))
        if self.waypoint:
            self.wx += dx
            self.wy += dy
        else:
            self.x += dx
            self.y += dy

    def move(self, instruction: str) -> None:
        cmd: str = instruction[0]
        amount: int = int(instruction[1:])
        if cmd in directions:
            self.navigate(amount, degree=directions[cmd])
        elif cmd == 'F':
            self.navigate(amount)
        else:
            diff = amount if cmd == 'R' else -amount
            if self.waypoint:
                size = sqrt(self.wx**2 + self.wy**2)
                d = degrees(atan2(self.wy, self.wx))
                d -= diff
                self.wx = size * cos(radians(d))
                self.wy = size * sin(radians(d))
            else:
                self.d = (self.d + diff) % 360

    def follow(self, file: str) -> None:
        instructions = file.strip().split('\n')
        for instruction in instructions:
            self.move(instruction)


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    txt = f.read()

    ship = Ship()
    ship.follow(txt)
    print(ship)
    print(ship.distance)

    ship = Ship(waypoint=True)
    ship.follow(txt)
    print(ship)
    print(ship.distance)
