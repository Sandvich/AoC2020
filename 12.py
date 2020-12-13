#!/usr/bin/env python3

def load_file():
    data = []
    with open('12.txt', 'r') as f:
        for line in f:
            data.append([line[0], int(line[1:])])
    return data

def run_instruction_simple(instruction, x, y, facing):
    facing_to_str = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    # Cardinal directions
    if instruction[0] == 'N':
        y += instruction[1]
    elif instruction[0] == 'S':
        y -= instruction[1]
    elif instruction[0] == 'E':
        x += instruction[1]
    elif instruction[0] == 'W':
        x -= instruction[1]
    # Rotation
    elif instruction[0] == 'L':
        facing += instruction[1]
        while facing >= 360:
            facing -= 360
    elif instruction[0] == 'R':
        facing -= instruction[1]
        while facing < 0:
            facing += 360
    # Forwards
    elif instruction[0] == 'F':
        new_instruction = [facing_to_str[facing], instruction[1]]
        return run_instruction_simple(new_instruction, x, y, facing)
    return x, y, facing

if __name__ == '__main__':
    data = load_file()
    x, y, facing = 0, 0, 0
    for instruction in data:
        x, y, facing = run_instruction_simple(instruction, x, y, facing)
    print(f'Final x: {x}\nFinal y: {y}\nFinal Facing: {facing}')
    print(f'Manhattan distance: {abs(x) + abs(y)}')
