#!/usr/bin/env python3
from collections import deque

def load_file():
    data = []
    with open('09.txt', 'r') as f:
        for line in f:
            data.append(int(line))
    return data

def xmas_sum(q, next_term):
    for first in q:
        for second in q:
            if first + second == next_term and first != second:
                return True
    return False

def test_xmas(data):
    q = deque(maxlen=25)
    for i in range(25):
        q.append(data[i])
    n = 25
    while n < len(data):
        if not xmas_sum(q, data[n]):
            print(f'Failed on line {n+1}')
            return data[n], n+1
        q.append(data[n])
        n += 1

def crack_xmas(data, weakness):
    for start_index in range(len(data)):
        for end_index in range(start_index, len(data)):
            sublist = data[start_index:end_index]
            if sum(sublist) == weakness:
                print(f'Sublist: {sublist}\nTotals: {sum(sublist)}')
                sublist.sort()
                return (sublist[0], sublist[-1])

if __name__ == '__main__':
    data = load_file()
    weakness, failure_line = test_xmas(data)
    print(f'The first number to fail the XMAS encyption scheme is {weakness}.')

    ans = crack_xmas(data[:failure_line], weakness)
    print(f'The sum of the first and last numbers in the weakness is {sum(ans)}.')
