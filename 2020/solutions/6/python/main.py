from os.path import join, dirname
from itertools import product
from typing import List, Set, Tuple
from functools import reduce


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    groups = f.read().strip().split('\n\n')

    at_least_one: List[int] = []
    everyone: List[int] = []
    for group in groups:
        answers: Set[str] = set()
        combined = None
        for answer in group.split('\n'):
            answer = answer.strip()
            as_set = set(list(answer))
            answers = answers.union(as_set)
            combined = as_set if combined == None else combined.intersection(
                as_set)
        at_least_one.append(len(answers))
        everyone.append(len(combined))
        # print(single)
        # print(reduce(lambda a, b: a.intersection(b), single))

    print(f'At least one person: {sum(at_least_one)}')
    print(f'Everyone: {sum(everyone)}')
