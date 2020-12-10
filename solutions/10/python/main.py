from os.path import join, dirname
from typing import List, Optional, Set, Tuple
from itertools import combinations, count
from math import floor, prod


def parse(s: str) -> List[int]:
    numbers: List[int] = sorted(map(int, s.strip().split('\n')))
    numbers.insert(0, 0)  # The wall
    numbers.append(numbers[-1] + 3)  # Phone itself
    return numbers


def diff(l: List[int]) -> List[int]:
    return [
        l[x] - l[x-1]
        for x in range(1, len(l))
    ]


def calc(d: List[int]) -> int:
    one = d.count(1)
    three = d.count(3)
    return one * three


def find_valid_permutations(d: List[int]) -> int:
    i = 0
    l = len(d)
    slices: List[int] = []
    while i < l:
        if d[i] != 3:
            try:
                n = d.index(3, i + 1)  # Find the next three
                diff = n - i
                if diff > 1:
                    slices.append(diff)
                    i = n
                    continue
            except:
                pass
        i += 1
    return prod([
        2**(s-1) - floor(s/4)
        for s in slices
    ])


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    numbers: List[int] = parse(f.read())
    d = diff(numbers)
    print(calc(d))
    print(find_valid_permutations(d))
