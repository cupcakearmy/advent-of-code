from typing import List
from itertools import product
from os.path import join, dirname

target = 2020
data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    numbers: List[int] = list(map(int, f.readlines()))
    for a, b in product(numbers, numbers):
        if a + b == target:
            print(f'The numbers: {a} and {b}.\tSolution: {a*b}')
            break

    for a, b, c in product(numbers, numbers, numbers):
        if a + b + c == target:
            print(f'The numbers: {a}, {b} and {c}.\tSolution: {a*b*c}')
            break
