import re


def part1(data):
    n_valid = 0
    for lo, hi, letter, password in data:
        n_valid += (lo <= sum(l == letter for l in password) <= hi)
    return n_valid


def part2(data):
    n_valid = 0
    for lo, hi, letter, password in data:
        n_valid += ((password[lo-1] == letter) ^ (password[hi-1] == letter))
    return n_valid


def main():
    pattern = '(\d+)-(\d+) (\w): (\w+)'
    compiled_regex = re.compile(pattern)
    data = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            lo, hi, letter, password = compiled_regex.search(line).groups()
            data.append((int(lo), int(hi), letter, password))
            line = f.readline()

    n_valid_1 = part1(data)
    print("Part 1:", n_valid_1)

    n_valid_2 = part2(data)
    print("Part 2:", n_valid_2)


if __name__ == '__main__':
    main()
