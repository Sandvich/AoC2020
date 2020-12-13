#!/usr/bin/env python3

def load_file():
    data = []
    with open('12.txt', 'r') as f:
        for line in f:
            data.append([line[0], int(line[1:])])
    return data

class SimpleRunner:
    # Cardinal directions
    def N(self, amount):
        self.y += amount
    def S(self, amount):
        self.y -= amount
    def E(self, amount):
        self.x += amount
    def W(self, amount):
        self.x -= amount

    # Rotation
    def L(self, amount):
        self.facing += amount
        self.facing = self.facing % 360
    def R(self, amount):
        self.facing -= amount
        self.facing = self.facing % 360

    # Forwards
    def F(self, amount):
        eval(f'self.{self.facing_to_str[self.facing]}({amount})')

    # Generic useful functions
    def __init__(self):
        self.facing_to_str = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
        self.x, self.y, self.facing = 0, 0, 0
    def run(self, instruction):
        eval(f'self.{instruction[0]}({instruction[1]})')
    def manhattan(self):
        return abs(self.x) + abs(self.y)
    def __repr__(self):
        return f'Instance of SimpleRunner.\nX: {self.x}, Y: {self.y}\nManhattan: {self.manhattan()}'

class ComplexRunner(SimpleRunner):
    def __init__(self):
        super().__init__()
        # We're defining the original x and y to be the waypoint to avoid rewriting the cardinal
        # functions with only minor changes
        self.ship_x, self.ship_y = 0, 0
        self.x, self.y = 10, 1
    def manhattan(self): # Need to adjust this instead of the cardinal functions
        return abs(self.ship_x) + abs(self.ship_y)
    def __repr__(self):
        return f'Instance of ComplexRunner.\nX: {self.ship_x}, Y: {self.ship_y}\nManhattan: {self.manhattan()}'

    # Rotation
    def L(self, amount):
        amount = int(amount / 90)
        for rotation in range(amount):
            self.x, self.y = -self.y, self.x
    def R(self, amount):
        self.L(360 - amount)

    # Forwards
    def F(self, amount):
        self.ship_x += amount*self.x
        self.ship_y += amount*self.y

if __name__ == '__main__':
    data = load_file()
    first, second = SimpleRunner(), ComplexRunner()
    for instruction in data:
        first.run(instruction)
        second.run(instruction)
    for runner in [first, second]:
        print(str(runner))
