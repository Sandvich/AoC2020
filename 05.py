#!/usr/bin/env python3

def load_file():
    with open("05.txt", "r") as f:
        data = []
        for line in f:
            data.append([line[:7], line[7:-1]])
    return data

def calculate_seat_id(data):
    row = int(
        data[0]
        .replace('F', '0')
        .replace('B', '1'),
    2)
    column = int(
        data[1]
        .replace('L', '0')
        .replace('R', '1'),
    2)
    return row*8+column

if __name__ == '__main__':
    data = load_file()
    seat_ids = []
    for boarding_pass in data:
        seat_ids.append(calculate_seat_id(boarding_pass))
    print(f'Highest seat ID: {max(seat_ids)}')
