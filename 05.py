#!/usr/bin/env python3

def load_file():
    with open("05.txt", "r") as f:
        data = []
        for line in f:
            data.append([line[:7], line[7:-1]])
    return data

def calculate_seat(data):
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
    return row, column

def calculate_seat_id(data):
    row, column = calculate_seat(data)
    return row*8+column

if __name__ == '__main__':
    data = load_file()
    seat_ids = []

    for boarding_pass in data:
        seat_ids.append(calculate_seat_id(boarding_pass))
    highest = max(seat_ids)
    print(f'Highest seat ID: {highest}')
    
    all_seats = [x for x in range(highest)]
    empty_seats = list(filter(lambda a: a not in seat_ids, all_seats))
    # create a list of the items in only one of the two lists of seats

    for seat in empty_seats:
        if seat > 8 and seat < highest - 8:
            # filter out those in the first and last rows
            if (seat-8) not in empty_seats and (seat+8) not in empty_seats:
                # filter out those in early or late rows
                myseat = seat

    print(f'My seat is: {myseat}')
