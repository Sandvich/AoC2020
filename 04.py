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

    @property
    def byr(self):
        return self.__byr
    @byr.setter
    def byr(self, byr):
        self.__byr = byr
        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            self._strictValid = False

    @property
    def iyr(self):
        return self.__iyr
    @iyr.setter
    def iyr(self, iyr):
        self.__iyr = iyr
        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
            self._strictValid = False

    @property
    def eyr(self):
        return self.__eyr
    @ eyr.setter
    def eyr(self, eyr):
        self.__eyr = eyr
        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
            self._strictValid = False

    @property
    def hgt(self):
        return self.__hgt
    @hgt.setter
    def hgt(self, hgt):
        self.__hgt = hgt
        try:
            height = int(hgt[:-2])
            unit = hgt[-2:]
            if unit == 'cm':
                if height < 150 or height > 193:
                    self._strictValid = False
            elif unit == 'in':
                if height < 59 or height > 76:
                    self._strictValid = False
            else:
                self._strictValid = False
        except ValueError:
            self._strictValid = False

    @property
    def hcl(self):
        return self.__hcl
    @hcl.setter
    def hcl(self, hcl):
        self.__hcl = hcl
        valid = True
        try:
            int(hcl[1:], 16)
            if hcl[0] != '#' or len(hcl) != 7:
                self._strictValid = False
        except ValueError:
            self._strictValid = False
        
    @property
    def ecl(self):
        return self.__ecl
    @ecl.setter
    def ecl(self, ecl):
        self.__ecl = ecl
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self._strictValid = False
    
    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, pid):
        self.__pid = pid
        try:
            int(pid)
            if len(pid) != 9:
                self._strictValid = False
        except ValueError:
            self._strictValid = False
    
    @property
    def cid(self):
        return self.__cid
    @cid.setter
    def cid(self, cid):
        self.__cid = cid

    def __init__(self, data):
        self._strictValid = True
        data = data.split()
        for item in self._fields:
            setattr(self, "_Passport__" + item, None)
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
        # This validation is far from perfect, as it allows invalid values to allow us to calculate part 1.
        # This means that invalid values can be set and therefore invalid instances can be created, and there's no way
        # to check if they return to being valid after being updated.
        return self.isValid() and self._strictValid
    
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
