import sys


def part1_result(one_cup, n_cups):
    res = []
    current = one_cup.next
    while len(res) < n_cups - 1:
        res.append(str(current.label))
        current = current.next
    return ''.join(res)


def part2_result(one_cup, n_cups):
    return one_cup.next.label * one_cup.next.next.label


class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None


def play(cups, n_moves, result_fn):
    n_cups = len(cups)
    min_label = min(cups)
    max_label = max(cups)

    cups = [Cup(label) for label in cups]
    for i in range(n_cups):
        cups[i].next = cups[(i + 1) % n_cups]

    # direct mapping to each cup
    label_to_cup = {cup.label: cup for cup in cups}

    current = cups[0]

    for move in range(n_moves):
        label = current.label
        # remove next 3 cups
        sl = [current.next, current.next.next, current.next.next.next]
        sl_labels = {c.label for c in sl}
        current.next = sl[-1].next

        # get next destination cup which is not a part of current slice
        # (can wrap around)
        destination_label = label - 1
        if destination_label < min_label:
            destination_label = max_label
        while destination_label in sl_labels:
            destination_label -= 1
            if destination_label < min_label:
                destination_label = max_label
        destination = label_to_cup[destination_label]

        # insert slice back into cups
        old_destination_next = destination.next
        destination.next = sl[0]
        sl[-1].next = old_destination_next

        # update new current cup to be the next one from the current
        current = current.next

    one_cup = label_to_cup[1]
    return result_fn(one_cup, n_cups)


def main(input_file):
    with open(input_file, 'r') as f:
        cups = [int(d) for d in f.read().strip()]

    val1 = play(cups[:], 100, part1_result)
    print('Part 1:', val1)

    cups.extend(range(10, 1000000+1))
    val2 = play(cups, 10000000, part2_result)
    print('Part 2:', val2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
