#!/usr/bin/env python3
import math

def load_file():
    lower, upper = [], []
    with open('01.txt', 'r') as f:
        for line in f:
            data = int(line)
            if data < 1010:
                lower.append(data)
            else:
                upper.append(data)
    return lower, upper

def two_matching(lower, upper):
    for first in lower:
        for second in upper:
            if first + second == 2020:
                return [first, second]

def three_matching(lower, upper):
    for first in lower:
        for second in lower:
            for third in lower + upper:
                if first + second + third == 2020:
                    return [first, second, third]

if __name__ == '__main__':
    lower, upper = load_file()
    answer = two_matching(lower, upper)
    print(f'Two entries which total 2020: {answer[0]} + {answer[1]}')
    print(f'Which multiply to: {math.prod(answer)}')
    answer = three_matching(lower, upper)
    print(f'Three entries which total 2020: {answer[0]} + {answer[1]} + {answer[2]}')
    print(f'Which multiply to: {math.prod(answer)}')
