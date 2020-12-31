import sys


def wrapped_slice(cups, i, k):
    n = len(cups)
    # wrap around slice of `k` elements starting at index `i`
    if i + k <= n:
        s = cups[i:i+k]
        del cups[i:i+k]
    else:
        s = cups[i:] + cups[:i+k-n]
        del cups[i:]
        del cups[:i+k-n]
    return s


def part1(cups):
    n = len(cups)
    idx = 0
    min_label = min(cups)
    max_label = max(cups)

    for _ in range(100):
        label = cups[idx]

        sl = wrapped_slice(cups, idx+1, 3)

        # destination must not be in slice, and wraps around
        destination = label - 1
        if destination < min_label:
            destination = max_label
        while destination in sl:
            destination -= 1
            if destination < min_label:
                destination = max_label
        new_idx = cups.index(destination)
        cups = cups[:new_idx+1] + sl + cups[new_idx+1:]

        # BAD ASSUMPTION: can only move 2 elements if slice wrapped around
        #if new_idx < idx:
        #    # slice was inserted before current cup, so add 3
        #    idx = (idx + 3) % n

        # index of our current label has now changed
        idx = cups.index(label)

        # new cup is at next index
        idx = (idx + 1) % n

    res = cups[cups.index(1)+1:] + cups[:cups.index(1)]
    res = ''.join(str(d) for d in res)
    return res


def part2():
    return None


def main(input_file):
    with open(input_file, 'r') as f:
        cups = [int(d) for d in f.read().strip()]
    #cups = [int(d) for d in "389125467"]
    val = part1(cups)
    print('Part 1:', val)


    val = part2()
    print('Part 1:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
