from typing import List, Union, Tuple, Set, Self
from dataclasses import dataclass

type Point = Tuple[int, int]

TURN = {
    # (-1,0) > (0, 1) -> (1, 0) -> (0, -1)
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


@dataclass
class Map:
    fields: List[List[bool]]
    position: Point
    direction: Point
    max_y: int = 0
    max_x: int = 0

    def __post_init__(self):
        self.max_y = len(self.fields)
        self.max_x = len(self.fields[0])

    def next_step(self):
        return (
            self.position[0] + self.direction[0],
            self.position[1] + self.direction[1],
        )

    def get(self, point: Point) -> Union[bool, None]:
        y, x = point
        try:
            return self.fields[y][x]
        except IndexError:
            return None

    def walk(self):
        visited: Set[Point] = set()
        while True:
            visited.add(self.position)
            next_step = self.next_step()
            content = self.get(next_step)
            if content is None:
                # Exited map
                break
            if content:
                # Turn
                self.direction = TURN[self.direction]
                next_step = self.next_step()
            self.position = next_step

        return len(visited)

    @staticmethod
    def parse(raw: str) -> Self:
        fields = [[f == "#" for f in line] for line in raw.splitlines()]
        # Find init
        position = (0, 0)
        direction = (-1, 0)  # Up
        for y, line in enumerate(raw.splitlines()):
            for x, f in enumerate(line):
                if f == "^":
                    position = (y, x)
        return Map(fields, position, direction)


def solve(raw: str) -> int:
    # Part 1
    part1 = 0
    part2 = 0

    m = Map.parse(raw)
    part1 = m.walk()

    return (part1, part2)


# Test
with open("./2024/06/test.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)

# Input
with open("./2024/06/input.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)
