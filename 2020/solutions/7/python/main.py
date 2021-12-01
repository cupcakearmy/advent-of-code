from os.path import join, dirname
from typing import Dict, List, Set, Tuple
import re

TRules = Dict[str, Dict[str, int]]


def split_trim(input: str, split: str) -> List[str]:
    return list(map(lambda s: s.strip(), input.split(split)))


def extract_inner(input: str) -> Tuple[int, str]:
    parts = input.split(' ')
    amount = int(parts[0])
    color = ' '.join(parts[1:-1])
    return amount, color


def parse_rules(rules: str) -> TRules:
    d: TRules = {}
    for rule in rules.strip().split('\n'):
        outer, inner = split_trim(rule, 'contain')
        outer = re.sub(r'bags?', '', outer).strip()
        d[outer] = {
            color: amount
            for amount, color in [
                extract_inner(i)
                for i in split_trim(inner, ',')
                if 'no other bag' not in i  # Also matches "bags"
            ]
        }
    return d


def find_enclosing_bags(rules: TRules, color: str) -> Set[str]:
    colors: Set[str] = set()
    stack: Set[str] = set([color])

    while len(stack):
        for item in list(stack):
            stack.remove(item)
            for contains, enclosing in rules.items():
                if item in enclosing:
                    if contains not in colors:
                        stack.add(contains)
                        colors.add(contains)
    return colors


def count_containing(rules: TRules, color: str) -> int:
    children = rules[color]
    if not children:
        return 0

    return sum([
        amount + amount * count_containing(rules, clr)
        for clr, amount in children.items()
    ])


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    rules = parse_rules(f.read())

    color = 'shiny gold'
    first = len(find_enclosing_bags(rules, color))
    print(f'We can pack the {color} into {first} bags')

    second = count_containing(rules, color)
    print(f'We need to put {second} bags into {color}')
