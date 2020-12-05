import re
import sys


def to_decimal(s, one_tokens):
    '''
    Converts a string representing a binary number to decimal.
    For example,

      >> to_decimal('FBFBBFFRLR', {'B','R'})
      357

    since this would be 0101100100 in binary.
    '''
    res = 0
    n_bits = len(s)
    for i in range(n_bits):
        res |= (s[i] in one_tokens) << (n_bits-1-i)
    return res


def get_seat_id(seat):
    '''
    It's just a binary number in disguise.
    '''
    one_tokens={'B', 'R'}
    return to_decimal(seat, one_tokens)


def part1(seats):
    '''
    Each seat can be thought of as two binary numbers. For instance, the seat
    'FBFBBFFRLR' is column 'FBFBBFF' and row 'RLR'. We can convert these into
    the binary numbers '0101100' and '101' which corresponds to column 44
    and row 5.
    '''
    max_seat_id = -1
    for seat in seats:
        seat_id = get_seat_id(seat)
        max_seat_id = max(max_seat_id, seat_id)
    return max_seat_id


def part2(seats):
    '''
    All seat ids should be contiguous, with the exception of one missing
    seat. This is my seat.
    '''
    seat_ids = [get_seat_id(seat) for seat in seats]
    seat_ids.sort()
    for i in range(len(seat_ids)):
        if seat_ids[i+1] - seat_ids[i] == 2:
            return seat_ids[i] + 1
    raise Exception('All seats taken')


def main(input_file):
    with open(input_file, 'r') as f:
        passes = [l.strip() for l in f.readlines()]

    highest_id = part1(passes)
    print("Part 1:", highest_id)

    my_seat_id = part2(passes)
    print("Part 2:", my_seat_id)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
