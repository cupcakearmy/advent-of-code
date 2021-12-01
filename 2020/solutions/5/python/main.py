from os.path import join, dirname
from itertools import product
from typing import Tuple


def from_binary(code: str, high: str) -> int:
    return int(''.join([
        '1' if char == high else '0'
        for char in code
    ]), 2)


def read_seat(seat) -> Tuple[int, int]:
    row_raw = seat[:-3]
    column_raw = seat[-3:]
    row = from_binary(row_raw, 'B')
    column = from_binary(column_raw, 'R')
    return row, column


def seat_code(row: int, column: int) -> int:
    return row * 8 + column


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    seats = f.read().strip().split('\n')

    free = list(product(range(4, 126), range(8)))
    maximum = 0
    for seat in seats:
        row, column = read_seat(seat)
        m = row * 8 + column
        maximum = max(maximum, m)
        free.remove((row, column))

    print(f"Highers ID:\t{maximum}")

    # Find the remaining seat
    row_max = 0
    row_min = 128
    for row, _ in free:
        row_max = max(row_max, row)
        row_min = min(row_min, row)
    remaining = [
        (row, column)
        for row, column in free
        if row >= row_min + 1 and row <= row_max - 2
    ][0]
    my_ticket = seat_code(*remaining)
    print(f"My Ticket:\t{my_ticket}")
