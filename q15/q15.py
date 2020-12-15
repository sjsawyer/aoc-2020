import sys


def part1(data, target):
    mem = {}
    i = 1
    for d in data[:-1]:
        mem[d] = i
        i += 1

    prev = data[-1]
    while i < target:
        if prev in mem:
            speak = i - mem[prev]
        else:
            speak = 0

        mem[prev] = i
        prev = speak
        i += 1

    return prev


def part2(data, target):
    return part1(data, target)


def main(input_file):
    with open(input_file, 'r') as f:
        data = [int(d) for d in f.read().split(',')]

    res1 = part1(data, 2020)
    print("Part 1:", res1)

    res2 = part2(data, 30000000)
    print("Part 2:", res2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
