import re
import sys


def part1(passports):
    mandatory_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    n_valid = 0
    for passport in passports:
        n_valid += all(field in passport for field in mandatory_fields)
    return n_valid


def part2(passports):

    validator = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (
            (x.endswith('cm') and 150 <= int(x[:-2]) <= 193)
            or (x.endswith('in') and 59 <= int(x[:-2]) <= 76)),
        'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
        'ecl': lambda x: x in {
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: re.match('^[0-9]{9}$', x),
        'cid': lambda x: True,
    }

    n_valid = 0

    for passport in passports:
        # All fields except 'cid' must be present
        if not all(field in passport for field in validator
                   if field != 'cid'):
            continue
        # Now validate the value of each field
        for field in passport:
            valid = ((field in validator)
                     and validator[field](passport[field]))
            if not valid:
                break
        else:
            n_valid += 1

    return n_valid


def main(input_file):
    with open(input_file, 'r') as f:
        content = f.read().split('\n\n')
    passports = []
    for block in content:
        passport = {}
        lines = block.strip().split('\n')
        for line in lines:
            entries = line.split(' ')
            for entry in entries:
                key, val = entry.split(':')
                passport[key] = val
        passports.append(passport)

    n_valid_1 = part1(passports)
    print("Part 1:", n_valid_1)

    n_valid_2 = part2(passports)
    print("Part 2:", n_valid_2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
