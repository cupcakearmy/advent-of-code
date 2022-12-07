#!/usr/bin/env python

from dataclasses import dataclass
from os.path import dirname, join
from typing import Callable, ClassVar, Literal, Union

# Day 07

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()


test = read_input('test.txt')
data = read_input('input.txt')


@dataclass
class File:
    size: int


@dataclass
class Directory:
    name: str
    contents: dict[str, Union['Directory', File]]
    parent: Union[None, 'Directory'] = None
    _size: int | None = None

    def size(self) -> int:
        if self._size is None:
            self._size = sum([
                entry.size if isinstance(entry, File) else entry.size()
                for entry in self.contents.values()
            ])
        return self._size

    def walk(self, fn: Callable[[Union[File, 'Directory']], None]):
        for entry in self.contents.values():
            fn(entry)
            if isinstance(entry, Directory):
                entry.walk(fn)


@dataclass
class Command:
    command: str
    output: list[str]


@dataclass
class Shell:
    commands: list[Command]
    root: Directory
    cwd: Directory

    def execute(self):
        for command in self.commands:
            cmd, *args = command.command.split()
            match cmd:
                case 'ls':
                    for entry in command.output:
                        size, name = entry.split()
                        self.cwd.contents[name] = Directory(name, {}, self.cwd) if size == 'dir' else File(int(size))
                case 'cd':
                    match args[0]:
                        case  '/':
                            self.cwd = self.root
                        case '..':
                            self.cwd = self.cwd.parent
                        case _:
                            self.cwd = self.cwd.contents[args[0]]

    def get_all_sizes(self) -> list[int]:
        sizes: list[int] = []

        def fn(entry: Directory | File):
            if isinstance(entry, Directory):
                sizes.append(entry.size())
        self.root.walk(fn)
        return sizes

    def flag_1(self):
        directories = self.get_all_sizes()
        return sum([size for size in directories if size <= 100_000])

    def flag_2(self, total=70_000_000, needed=30_000_000):
        to_remove = needed - total + self.root.size()
        big_enough = sorted([
            size
            for size in self.get_all_sizes()
            if size > to_remove
        ])
        return big_enough[0]

    @staticmethod
    def parse(data: str):
        commands = [command.strip().split('\n') for command in data.split('$ ')[1:]]
        root = Directory('/', {})
        return Shell([Command(command[0], command[1:]) for command in commands], root, root)


shell = Shell.parse(test)
shell.execute()
print(shell.flag_1())
print(shell.flag_2())

shell = Shell.parse(data)
shell.execute()
print(shell.flag_1())
print(shell.flag_2())
