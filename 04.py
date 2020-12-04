#!/usr/bin/env python3

class Passport:
    _fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid'
    ]

    def __init__(self, data):
        data = data.split()
        for item in self._fields:
            setattr(self, item, None)
        for item in data:
            splititem = item.split(':')
            if splititem[0] in self._fields:
                setattr(self, splititem[0], splititem[1])
    
    def isValid(self):
        for item in self._fields:
            if getattr(self, item) is None and item != 'cid':
                return False
        return True
    
    def isValidStrict(self):
        # Note: all these checks return False. If nothing returns, we follow through to the final return, which is True
        # Birth Year validation
        if self.byr is None or len(self.byr) != 4 or int(self.byr) < 1920 or int(self.byr) > 2002:
            return False
        # Issue Year validation
        if self.iyr is None or len(self.iyr) != 4 or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False
        # Expiration Year validation
        if self.eyr is None or len(self.eyr) != 4 or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False
        # Height validation
        if self.hgt is None or self.hgt[-2:] not in ["cm", 'in']:
            return False
        height = int(self.hgt[:-2])
        if self.hgt[-2:] == 'cm':
            if height < 150 or height > 193:
                return False
        if self.hgt[-2:] == 'in':
            if height < 59 or height > 76:
                return False
        # Hair Colour validation
        if self.hcl is None or self.hcl[0] != '#' or len(self.hcl) != 7:
            return False
        try:
            int(self.hcl[1:], 16)
        except ValueError:
            return False
        # Eye Colour validation
        if self.ecl is None or self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        # Passport ID validation
        if self.pid is None or len(self.pid) != 9:
            return False
        try:
            int(self.pid)
        except ValueError:
            return False
        return True
    
    def __repr__(self):
        return f'\
Instance of Passport at {id(self)}\nBirth Year: {self.byr}\nIssue Year: {self.iyr}\nExpiry Year: {self.iyr}\nHeight: {self.hgt}\
\nHair Colour: {self.hcl}\nEye Colour: {self.ecl}\nPassport ID: {self.pid}\nCountry ID: {self.cid}'

def load_file():
    data = []
    constructor = []
    with open('04.txt', 'r') as f:
        for line in f:
            if line != "\n":
                constructor.append(line)
            else:
                data.append(Passport(" ".join(constructor)))
                constructor = []
    return data

if __name__ == '__main__':
    data = load_file()
    count, strict_count = 0, 0
    for passport in data:
        if passport.isValid():
            count += 1
        if passport.isValidStrict():
            strict_count += 1
    print(f'Number of valid passports: {count}')
    print(f'Number of valid passports (strict checking): {strict_count}')
