#!/usr/bin/env python3

def load_file():
    data = {}
    with open('07.txt', 'r') as f:
        for line in f:
            text = line.split('contain')
            text[1] = text[1].strip().split(',')
            outer = ' '.join(text[0].split()[:2])
            data[outer] = text[1]
    return data

def process_input(data):
    bags = {}
    for line in data.keys():
        bags[line] = []
        for i, bag in enumerate(data[line]):
            if bag != "no other bags.":
                rule = bag.split()
                bags[line].append([int(rule[0]), ' '.join(rule[1:3])])
    return bags

def bag_can_contain(data, bag, search):
    colours = [ x[1] for x in data[bag] ]
    if len(colours) == 0:
        return False
    elif search in colours:
        return True
    else:
        return any([bag_can_contain(data, x, search) for x in colours])

def count_contents(data, bag):
    retval = 1
    for item in data[bag]:
        retval += item[0] * count_contents(data, item[1])
    return retval

if __name__ == '__main__':
    my_bag = 'shiny gold'
    data = process_input(load_file())
    count = 0
    for bag in data:
        if bag_can_contain(data, bag, my_bag):
            count += 1
    my_bag_contains = count_contents(data, my_bag) - 1
    print(f'{count} different types of bag can contain one {my_bag} bag.')
    print(f'My {my_bag} bag needs to have {my_bag_contains} bags inside it.')
