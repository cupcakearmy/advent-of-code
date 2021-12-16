#!/usr/bin/env python

from os.path import join, dirname
from typing import List

# Day 10

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Node:
    def __init__(self, brackets, children):
        self.brackets = brackets
        self.children = children

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self) -> str:
        return f'{self.brackets} -> {len(self.children)} {self.children}'


class Parser:
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']

    def __init__(self, code: str):
        self.tollerant = False
        self.code = code
        self.pos = 0
        self.valid = True
        self.nodes: List[Node] = []

    def parse(self, tollerant=False):
        self.tollerant = tollerant
        root = Node(None, [])
        try:
            self.traverse(root)
        except Exception as e:
            # print(e.args[0])
            pass
        self.nodes.append(root)

    def traverse(self, node):
        c = self.code[self.pos]
        typ = self.openers.index(c) if c in self.openers else -1
        if typ == -1:
            self.valid = False
            raise Exception(
                f'Invalid character at position {self.pos}. Found {c}')

        node = Node(typ, [])
        while True:
            self.pos += 1
            closing = self.closers[typ]
            if self.pos >= len(self.code):
                if self.tollerant:
                    self.code += closing
                    break
                else:
                    raise Exception("EOF")
            c = self.code[self.pos]
            if c == closing:
                break
            else:
                node.add_child(self.traverse(node))
        return node


class Checker:
    def __init__(self, lines: List[str]):
        self.lines = [Parser(line) for line in lines]

    def flag1(self):
        for line in self.lines:
            line.parse(tollerant=False)
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        flag = [
            points[line.code[line.pos]]
            for line in self.lines
            if not line.valid
        ]
        return sum(flag)

    def flag2(self):
        added = ''
        for line in self.lines:
            print(f'\nChecking:')
            print(line.code)
            before = len(line.code)
            line.parse(tollerant=True)
            if line.valid:
                print(line.code)
                added += line.code[before:]

    @ staticmethod
    def parse(lines: str):
        return Checker(lines.split('\n'))


# 1
print('1.')
checker = Checker.parse(test)
print(f'Test: {checker.flag1()}')
checker = Checker.parse(data)
print(f'Real: {checker.flag1()}')

# 2
print('\n2.')

checker = Checker.parse(test)
print(f'Test: {checker.flag2()}')
