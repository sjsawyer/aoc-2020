import re
import sys
from functools import reduce


def part1(rules, other_tickets):
    ''' So turns out part2 is not that complicated; Oh well '''
    # extract all valid intervals
    intervals = []
    for r in rules:
        intervals.append(r[1:3])
        intervals.append(r[3:5])

    # combine overlapping intervals
    intervals.sort()
    collapsed_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= collapsed_intervals[-1][1]:
            new_interval = (collapsed_intervals[-1][0],
                            max(collapsed_intervals[-1][1],
                                intervals[i][1]))
            collapsed_intervals[-1] = new_interval
        else:
            collapsed_intervals.append(intervals[i])

    # now find all values not within any intervals
    def contained(k, intervals):
        for interval in intervals:
            if k < interval[0]:
                return False
            if interval[0] <= k <= interval[1]:
                return True
        return False

    err = 0
    valid_tickets = []
    for ticket in other_tickets:
        bad = False
        for val in ticket:
            if not contained(val, collapsed_intervals):
                bad = True
                err += val
        if not bad:
            valid_tickets.append(ticket)

    return err, valid_tickets


def part2(valid_tickets, my_ticket, rules):
    # transpose tickets to get all values per given category
    values = list(zip(*valid_tickets))

    def is_valid(vals, field_idx):
        a, b, c, d = rules[field_idx][1:]
        return all((a <= val <= b or c <= val <= d) for val in vals)

    fields = [rule[0] for rule in rules]
    assigned_fields = {}
    val_idxs = list(range(len(values)))

    while len(assigned_fields) < len(rules):
        for i, field in enumerate(fields):
            if field in assigned_fields:
                continue
            v = [is_valid(values[j], i) for j in val_idxs]
            if sum(v) == 1:
                k = v.index(True)
                assigned_fields[field] = val_idxs[k]
                del val_idxs[k]

    idxs = [assigned_fields[k] for k in assigned_fields
            if 'departure' in k]
    return reduce(lambda x,y: x*y,
                  (my_ticket[idx] for idx in idxs))


def main(input_file):

    with open(input_file, 'r') as f:
        content =  f.read().split('\n\n')

    rules = re.findall('([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', content[0])
    my_ticket = [int(n) for n in content[1].split('\n')[1].split(',')]
    other_tickets = [[int(n) for n in l.split(',')]
                     for l in content[2].rstrip().split('\n')[1:]]
    rules = [(rule[0], *map(int, rule[1:]))
             for rule in rules]

    err_rate, valid_tickets = part1(rules, other_tickets)
    print('Part 1:', err_rate)

    res = part2(valid_tickets, my_ticket, rules)
    print('Part 2:', res)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
