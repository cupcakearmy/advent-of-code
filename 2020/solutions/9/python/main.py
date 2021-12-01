from os.path import join, dirname
from typing import List, Optional, Set, Tuple
from itertools import combinations


class XMAS:

    def __init__(self, data: str, size: int) -> None:
        self.size: int = size
        self.position: int = size
        self.buffer: List[int] = [
            int(x)
            for x in data.strip().split('\n')
        ]

    def check_next(self) -> bool:
        possible = [
            a + b
            for a, b in combinations(self.buffer[self.position - self.size: self.position], 2)
        ]
        return self.buffer[self.position] in possible

    def find_first_invalid(self) -> int:
        l = len(self.buffer)
        while self.position < l:
            valid = self.check_next()
            if not valid:
                return self.buffer[self.position]
            self.position += 1
        raise Exception

    def find_slice(self, target: int):
        l = len(self.buffer)
        for n in range(l):
            for m in range(n, l):
                slice = self.buffer[n: m]
                if sum(slice) == target:
                    return min(slice) + max(slice)
        raise Exception


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    xmas = XMAS(f.read(), 25)

    first_invalid = xmas.find_first_invalid()
    print(first_invalid)

    solution = xmas.find_slice(first_invalid)
    print(solution)
