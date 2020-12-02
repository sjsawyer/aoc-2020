def part1(data, target_sum):
    '''
    Assumes data is sorted.

    Runtime (with sorting): n + n*log(n) = n*log(n)
    '''
    i, j = 0, len(data) - 1
    while i < j:
        if data[i] + data[j] == target_sum:
            return data[i], data[j]
        if data[i] + data[j] > target_sum:
            j -= 1
        else:
            i += 1
    raise Exception('no two numbers sum to {}'.format(target_sum))


def part2(data):
    '''
    For each item in data, attempt part1 with the new target sum.
    Assumes data is sorted.

    Runtime: n*log(n) + n + (n-1) + (n-2) + ... + 1 = O(n^2)

    '''
    while len(data) > 2:
        n3 = data.pop()
        try:
            # Assume n3 is part of the solution
            target_sum = 2020 - n3
            n1, n2 = part1(data, target_sum)
            return n1, n2, n3
        except:
            # Didn't work, try next value and continue without current n3
            # since n3 won't be part of the solution (we just tried all
            # possible solutions including n3 and none worked)
            pass
    raise Exception('no three numbers sum to 2020')


def main():
    with open('input.txt', 'rb') as f:
        data = [int(l) for l in f.readlines()]
    # critical to success is sorting
    data.sort()
    n1, n2 = part1(data, 2020)
    print('part 1:', (n1, n2), n1*n2)
    n1, n2, n3 = part2(data)
    print('part 2:', (n1, n2, n3), n1*n2*n3)


if __name__ == '__main__':
    main()
