from os.path import join, dirname
from typing import List, Optional, Set, Tuple

Instructions = List[Tuple[str, int]]


class VM:
    def __init__(self, code: str) -> None:
        instructionsRaw = code.strip().split('\n')
        self.acc = 0
        self.oc = 0
        self.invert: Optional[int] = None
        self.instructions: Instructions = []
        for instruction in instructionsRaw:
            op, value = instruction.split(' ')
            self.instructions.append((op, int(value)))

    def reset(self):
        self.acc = 0
        self.oc = 0

    def exec(self):
        op, value = self.instructions[self.oc]
        if self.oc == self.invert:
            op = 'jmp' if op == 'nop' else 'nop'
        if op == 'nop':
            self.oc += 1
        elif op == 'acc':
            self.acc += value
            self.oc += 1
        elif op == 'jmp':
            self.oc += value

    def run(self) -> Tuple[int, bool]:
        self.reset()
        already_visited: Set[int] = set()
        m = len(self.instructions)
        while True:
            if self.oc in already_visited:
                return (self.acc, True)
            if not self.oc < m:
                return (self.acc, False)
            already_visited.add(self.oc)
            self.exec()

    def fix(self):
        for i, instruction in enumerate(self.instructions):
            op, _ = instruction
            if op == 'nop' or op == 'jmp':
                self.invert = i
                acc, error = self.run()
                if not error:
                    return acc


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    vm = VM(f.read())

    acc, err = vm.run()
    print(acc)

    print(vm.fix())
