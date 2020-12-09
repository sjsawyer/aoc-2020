import sys


def part1(data):
    window_len = 25
    window = set(data[:window_len])
    idx = window_len
    while True:
        n = data[idx]
        # Find two numbers in current window that sum to n
        for m in data[idx-window_len:idx]:
            if n - m in window and n - m != m:
                # found
                window.remove(data[idx-window_len])
                window.add(n)
                idx += 1
                break
        else:
            return n


def part2(data, target_sum):
    i, j = 0, 0
    current_sum = data[0]
    while j < len(data):
        if current_sum < target_sum:
            j += 1
            current_sum += data[j]
        elif current_sum > target_sum:
            current_sum -= data[i]
            i += 1
        else:
            return min(data[i:j+1]) + max(data[i:j+1])

    raise Exception('no contiguous subsequence sums to target')


def main(input_file):

    with open(input_file, 'r') as f:
        data = [int(l) for l in f.readlines()]

    val_1 = part1(data)
    print('Part 1:', val_1)

    val_2 = part2(data, val_1)
    print('Part 2:', val_2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
