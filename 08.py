#!/usr/bin/env python3
import copy

class InfiniteLoopError(Exception):
    def __init__(self, message="Infinite loop detected."):
        self.message = message
        super().__init__(self.message)

class BootLoader:
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, newcode):
        if self.executed:
            raise RuntimeError("Cannot add code after boot!")
        self.__code = newcode
        self.length = len(self.code)
    def change_code(self, line, cmd):
        oldcode = self.code
        oldcode[line] = cmd
        self.code = oldcode

    def __init__(self, code):
        self.executed = False
        self.code = copy.deepcopy(code)
        self.lines_executed = []
        self.accumulator = 0
        self.next_line = 0
    
    def acc(self, value):
        self.accumulator += int(value)
        self.next_line += 1
    def jmp(self, value):
        self.next_line += int(value)
    def nop(self, value):
        self.next_line += 1
    def execute(self):
        self.executed = True
        while self.next_line < self.length:
            if self.next_line in self.lines_executed:
                raise InfiniteLoopError()
            self.lines_executed.append(self.next_line)
            command = self.code[self.next_line].split()
            eval(f'self.{command[0]}({command[1]})')
        return self.accumulator

def load_file():
    data = []
    with open('08.txt', 'r') as f:
        for line in f:
            data.append(line)
    return data

def fix_bootloader(line, data):
    boot = BootLoader(data)
    command, original = data[line].split(), data[line].strip()
    change_to = None
    if command[0] == 'jmp':
        change_to = f'nop {command[1]}'
    elif command[0] == 'nop':
        change_to = f'jmp {command[1]}'
    try:
        if change_to is not None:
            boot.change_code(line, change_to)
            assert(boot.code[line] == change_to)
            acc = boot.execute()
            print('\nExecution succeeded!')
            print(f'line changed: {line}')
            print(f'accumulator value: {acc}')
            return True
    except InfiniteLoopError:
            return False

if __name__ == '__main__':
    data = load_file()
    boot = BootLoader(data)
    try:
        boot.execute()
    except InfiniteLoopError:
        print(f'boot lines executed: {boot.lines_executed}')
        print(f'boot failed trying to run line: {boot.next_line}')
        print(f'accumulator value at crash: {boot.accumulator}')
    
    potential_error_lines = boot.lines_executed
    for line in potential_error_lines:
        if fix_bootloader(line, data):
            quit()
        