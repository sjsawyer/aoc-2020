import sys


def part1(data):
    data.sort()
    aug_data = [0] + data + [data[-1]+3]
    diffs = [x-y for x,y in zip(aug_data[1:], aug_data[:-1])]
    return diffs.count(1)*diffs.count(3)


def part2(data):
    # already sorted from part1 but let's just be extra sure :P
    data.sort()
    aug_data = [0] + data + [data[-1]+3]

    # dp[i] is the number of ways to get to aug_data[i], which we will
    # calculate bottom up
    dp = [None for _ in range(len(aug_data))]
    dp[0] = 1

    for i in range(1, len(aug_data)):
        dp[i] = sum(dp[i-j] if i-j>=0 and aug_data[i] - aug_data[i-j] <= 3
                    else 0 for j in range(1, 4))
    return dp[-1]


def main(input_file):

    with open(input_file, 'r') as f:
        data = [int(l) for l in f.readlines()]

    val = part1(data)
    print('Part 1:', val)

    total_paths = part2(data)
    print('Part 2:', total_paths)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
