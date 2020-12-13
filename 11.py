#!/usr/bin/env python3
from copy import deepcopy

def load_file():
    data = []
    mapping = {'.': None, 'L': 0, '#': 1}
    with open('11.txt', 'r') as f:
        for line in f:
            data.append([])
            for character in line.strip():
                data[-1].append(mapping[character])
    return data

def calculate_occupancy(rows, cols, data, current_value):
    if current_value is None:
        return None
    
    occupied_seats = 0
    for row in rows:
        for column in cols:
            if data[row][column] is not None:
                occupied_seats += data[row][column]
    if occupied_seats - current_value == 0:
        return 1
    if occupied_seats - current_value >= 4:
        return 0
    else:
        return current_value

def run_iteration_first(data):
    newdata = []
    for row in range(len(data)):
        newdata.append([])
        consider_rows = [row]
        if row > 0:
            consider_rows.append(row - 1)
        if row < len(data) - 1:
            consider_rows.append(row + 1)
        for seat in range(len(data[row])):
            consider_cols = [seat]
            if seat > 0:
                consider_cols.append(seat - 1)
            if seat < len(data[row]) - 1:
                consider_cols.append(seat + 1)
            newdata[-1].append(calculate_occupancy(consider_rows, consider_cols, data, data[row][seat]))
    return newdata

def run_algorithm(to_run, data):
    iterations, stable = 0, False
    while not stable:
        iterations += 1
        newdata = to_run(data)
        print(f'Completed iteration {iterations}')
        comparison = []
        for row in zip(data, newdata):
            if all(i == j for i, j in zip(row[0], row[1])):
                comparison.append(True)
            else:
                comparison.append(False)
        if all(comparison):
            stable = True
        data = newdata
    occupied = 0
    for row in data:
        occupied += row.count(1)
    return iterations, occupied

if __name__ == '__main__':
    data = load_file()
    iterations, occupied = run_algorithm(run_iteration_first, deepcopy(data))
    print(f'Stable after {iterations} iterations (first algorithm). {occupied} seats occupied.')
    # iterations, occupied = run_algorithm(run_iteration_second, deepcopy(data))
    # print(f'Stable after {iterations} iterations (second algorithm). {occupied} seats occupied.')
