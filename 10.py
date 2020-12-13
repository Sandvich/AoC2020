#!/usr/bin/env python3

def load_file():
    data = []
    with open('10.txt', 'r') as f:
        for line in f:
            data.append(int(line))
    data.sort()
    return data

def jolt_diffs(chargers):
    chargers.insert(0, 0)
    chargers.append(chargers[-1]+3)
    diffs = [0,0,0,0]
    for i in range(1, len(chargers)):
        upjolt = chargers[i] - chargers[i-1]
        diffs[upjolt] += 1
    print(str(diffs))
    return diffs

if __name__ == '__main__':
    chargers = load_file()
    diffs = jolt_diffs(chargers)
    print(f'Multiplying the number of 1-jolt diffs by the number of 3-jolt diffs gives us {diffs[1]*diffs[3]}')
