from typing import List, Union, Tuple

Point = Tuple[int]
Path = Tuple[Point]
Paths = [Path]

ALL_DIRECTIONS = (
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
)

LETTER_MAP = {"X": 0, "M": 1, "A": 2, "S": 3}


class Board:
    rows: List[List[int]]

    def __init__(self, rows: List[List[int]]):
        self.rows = rows
        self.max_y = len(self.rows)
        self.max_x = len(self.rows[0])

    def get(self, x: int, y: int) -> Union[None, int]:
        if x < 0 or y < 0:
            return None
        if x >= self.max_x or y >= self.max_y:
            return None
        return self.rows[y][x]

    # def get_neighbours(self, x: int, y: int, target: int) -> List[Point]:
    #     n = []
    #     for dx in range(x - 1, x + 2):
    #         for dy in range(y - 1, y + 2):
    #             if self.get(dx, dy) == target:
    #                 n.append((dx, dy))
    #     return n

    @staticmethod
    def parse(raw: str):
        rows = [[LETTER_MAP[letter] for letter in line] for line in raw.splitlines()]
        return Board(rows)


# def find_maze(b: Board, path: Path, next_char: int) -> Paths:
#     x, y = path[-1]
#     print(f"Find {x} {y} n={next_char}")
#     paths: Paths = []
#     neighbours = b.get_neighbours(x, y, next_char)

#     # Found last letter
#     if next_char == 3:
#         return [path + (n,) for n in neighbours]

#     # Recurse
#     for n in neighbours:
#         p = path + (n,)
#         sub_paths = find(b, p, next_char + 1)
#         if len(sub_paths):
#             paths = paths + sub_paths

#     return paths


def find_line(b: Board, point: Point, direction: Point) -> Union[Path, None]:
    x, y = point
    dx, dy = direction
    path: Path = point
    for i in range(1, 4):
        px = x + (dx * i)
        py = y + (dy * i)
        if b.get(px, py) != i:
            return None
        path = path + ((x, y),)
    return path


def find_x(b: Board, point: Point) -> bool:
    x, y = point
    for dx, dy in ALL_DIRECTIONS:
        # Check if is "M", then the opposite for "S" and the the perpendicular
        if b.get(x + dx, y + dy) == 1:
            if b.get(x - dx, y - dy) == 3:
                # Found first "MAS", check perpendicular
                p_dx = -dy
                p_dy = dx
                p_a = b.get(x + p_dx, y + p_dy)
                p_b = b.get(x - p_dx, y - p_dy)
                if (p_a == 1 and p_b == 3) or (p_a == 3 and p_b == 1):
                    return True
    return False


def solve(raw: str) -> int:
    # Part 1
    part1 = []
    part2 = 0

    b = Board.parse(raw)

    for x in range(b.max_x):
        for y in range(b.max_y):
            p = b.get(x, y)
            if p == 0:
                for direction in ALL_DIRECTIONS:
                    found = find_line(b, (x, y), direction)
                    if found:
                        part1.append(found)

            if p == 2:
                if find_x(b, (x, y)):
                    part2 += 1

    return (len(part1), part2)


# Test
with open("./2024/04/test.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)

# Input
with open("./2024/04/input.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)
