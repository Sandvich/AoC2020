#!/usr/bin/env python3

def load_file():
    data = []
    with open('06.txt', 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def process_file_one(data):
    groups = []
    groups.append(set())
    for line in data:
        if len(line) == 0:
            groups.append(set())
        for character in line:
            groups[-1].add(character)
    return groups

def process_file_two(data):
    groups, current_group = [], []
    data.append('') # the last \n is ignored, so we need to add it back in to ensure the count is correct
    for line in data:
        if len(line) == 0:
            all_answered = set(current_group[0])
            for i in range(1, len(current_group)):
                all_answered = all_answered.intersection(current_group[i])
            current_group = []
            groups.append(all_answered)
        else:
            current_group.append([])
        for character in line:
            current_group[-1].append(character)
    return groups

def count_answers(groups):
    count = 0
    for i in groups:
        count += len(i)
    return count

if __name__ == '__main__':
    data = load_file()
    groups_one = process_file_one(data)
    groups_two = process_file_two(data)
    print(f'First count: {count_answers(groups_one)}')
    print(f'Second count: {count_answers(groups_two)}')
