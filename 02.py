#!/usr/bin/env python3

def load_file():
    rule, password = [], []
    with open("02.txt", "r") as f:
        for line in f:
            data = line.split()
            rule.append(f'{data[0]} {data[1][:-1]}')
            password.append(data[2])
    return rule, password

def test_password_first(rule, password):
    rule = rule.replace('-', ' ').split()
    count = 0
    for letter in password:
        if letter == rule[2]:
            count += 1
    if count >= int(rule[0]) and count <= int(rule[1]):
        return True
    return False

def test_password_second(rule, password):
    rule = rule.replace('-', ' ').split()
    first = password[int(rule[0])-1] == rule[2]
    second = password[int(rule[1])-1] == rule[2]
    if first and second:
        return False
    return first or second

if __name__ == '__main__':
    rules, passwords = load_file()
    first_count, second_count = 0, 0
    for i in range(len(rules)):
        if test_password_first(rules[i], passwords[i]):
            first_count += 1
        if test_password_second(rules[i], passwords[i]):
            second_count += 1
    
    print(f"Correct passwords according to the first rule:\t{first_count}\nCorrect passwords according to the second rule:\t{second_count}")
