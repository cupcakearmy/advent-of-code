from typing import List, Union, Tuple, Set
from dataclasses import dataclass
import networkx as nx
import matplotlib.pyplot as plt


@dataclass
class Node:
    id: int
    links: List


@dataclass
class Manual:
    rules: Tuple[int]
    updates: Tuple[int]

    def check_update(self, update: Tuple[int]) -> bool:
        cur = 0
        for n in update:
            if n not in self.order:
                continue
            m = self.order[n]
            if m < cur:
                return False
            cur = m
        return True

    def check(self):
        total = 0
        for update in self.updates:
            valid = self.check_update(update)
            if valid:
                total += update[len(update) // 2]
        return total

    def build_rules(self):
        unique: Set[int] = set()
        for rule in self.rules:
            unique.add(rule[0])
            unique.add(rule[1])
        nodes = {n: Node(id=n, links=[]) for n in unique}
        for start, end in self.rules:
            nodes[start].links.append(end)

        # Test
        G = nx.DiGraph()
        for rule in self.rules:
            G.add_edge(*rule)
        print(G.number_of_nodes())

        TR = nx.transitive_reduction(G)
        subax1 = plt.subplot(121)
        nx.draw(TR, with_labels=True, font_weight="bold")
        plt.show()

        sorted = list(nx.topological_sort(G))
        print(sorted)

        # Topological sorting
        # https://cs.stackexchange.com/a/29133
        order = {n: i for i, n in enumerate(sorted)}
        self.order = order

    @staticmethod
    def parse(raw: str):
        rules_raw, updates_raw = raw.strip().split("\n\n")
        rules = [tuple((map(int, line.split("|")))) for line in rules_raw.splitlines()]
        updates = [
            tuple(map(int, line.split(","))) for line in updates_raw.splitlines()
        ]
        return Manual(rules, updates)


def solve(raw: str) -> int:
    # Part 1
    part1 = 0
    part2 = 0

    m = Manual.parse(raw)
    m.build_rules()
    part1 = m.check()

    return (part1, part2)


# Test
with open("./2024/05/test.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)

# Input
with open("./2024/05/input.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)
