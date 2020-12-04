#!/usr/bin/env python3
import math

def load_file():
    with open("03.txt", "r") as f:
        data = []
        for line in f:
            data.append([])
            for column in line:
                if column == ".":
                    data[-1].append(0)
                elif column == "#":
                    data[-1].append(1)
    return data

def test_route(data, xdiff, ydiff=1):
    trees_encountered = 0
    index_x = 0
    if ydiff == 1:
        newdata = data
    elif ydiff > 1:
        newdata = data[::ydiff]

    for line in newdata:
        trees_encountered += line[index_x]
        index_x = (index_x + xdiff) % len(line)
    return trees_encountered

if __name__ == "__main__":
    data = load_file()
    trees = [
        test_route(data, 1),
        test_route(data, 3),
        test_route(data, 5),
        test_route(data, 7),
        test_route(data, 1,2)
    ]
    print(str(trees))
    print(str(math.prod(trees)))
