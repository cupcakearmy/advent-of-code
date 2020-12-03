from typing import Dict, List
from os.path import join, dirname
from functools import reduce


class Forest():

    def __init__(self, text: str) -> None:
        self.text = text.strip().split('\n')

    @property
    def height(self) -> int:
        return len(self.text)

    def is_tree_at(self, y: int, x: int) -> bool:
        if y > self.height:
            return False
        row = self.text[y]
        return row[x % len(row)] == '#'


data = join(dirname(__file__), 'data.txt')
with open(data) as f:
    forest = Forest(f.read())

    # 1
    trees: int = 0
    for y in range(forest.height):
        is_tree: bool = forest.is_tree_at(y, y*3)
        if is_tree:
            trees += 1
    print(f'Result Simple: {trees}')

    # 2
    all: Dict[str, int] = {
        '11': 0,
        '13': 0,
        '15': 0,
        '17': 0,
        '21': 0,
    }
    for i in range(forest.height):
        for key, value in all.items():
            dy, dx = map(int, list(key))
            y = i * dy
            x = i * dx
            if forest.is_tree_at(y, x):
                all[key] += 1
    total = reduce((lambda x, y: x * y), all.values())
    print(f'Result Combined: {list(all.values())} = {total}')
