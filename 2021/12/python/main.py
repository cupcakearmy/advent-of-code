#!/usr/bin/env python

from os.path import dirname, join

# Day 12

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


class Node:
    def __init__(self, name: str, children: set['Node']):
        self.name = name
        self.children = children
        self.big = name[0].isupper()

    def isSmall(self) -> bool:
        return self.name[0].islower()

    def __str__(self) -> str:
        return f'{self.name} -> {[node.name for node in self.children]}'

    def __repr__(self) -> str:
        return self.name


class Graph:
    start_node = 'start'
    end_node = 'end'

    def __init__(self, nodes: list):
        self.nodes = nodes

    def _find_node(self, name: str) -> Node:
        for node in self.nodes:
            if node.name == name:
                return node
        raise Exception(f'node "{name}" not found')

    def _find_routes(self, current_node: Node, visited: set[Node], joker: bool) -> list[list[Node]]:
        routes: list[list[Node]] = []

        # Iterate children
        for node in current_node.children:
            if node.name == Graph.start_node:
                continue
            if node.name == Graph.end_node:
                routes.append([node])
                continue

            # Check if is a small cave -> move on
            if not node.big and node in visited:
                # Part 2
                # If it's already visited, but we still have the "joker" left, we can use it
                if joker:
                    routes += self._find_routes(node, {*visited, node}, False)
                continue
            routes += self._find_routes(node, {*visited, node}, joker)
        return [[current_node, *route] for route in routes]

    def find_routes(self, allow_double=False):
        start_node = self._find_node(Graph.start_node)
        return self._find_routes(start_node, {start_node}, allow_double)

    @staticmethod
    def parse(text: str):
        links = [tuple(link.split('-')) for link in text.splitlines()]
        nodeNames = set()
        for link in links:
            nodeNames.add(link[0])
            nodeNames.add(link[1])
        nodes = {
            name: Node(name, set())
            for name in nodeNames
        }
        for start, end in links:
            nodes[start].children.add(nodes[end])
            nodes[end].children.add(nodes[start])

        return Graph(list(nodes.values()))


# 1
print('1.')

graph = Graph.parse(test)
print(len(graph.find_routes()))
graph = Graph.parse(data)
print(len(graph.find_routes()))

# 2
print('\n2.')
graph = Graph.parse(test)
print(len(graph.find_routes(True)))
graph = Graph.parse(data)
print(len(graph.find_routes(True)))
