import sys
from functools import reduce


def part1(departure_time, buses):
    buses = [bus for bus in buses if bus is not None]
    opt_bus = min(buses, key=lambda bus: bus - departure_time % bus)
    return opt_bus*(opt_bus - departure_time % opt_bus)


def solve(x, d, m):
    # find n st n*x == d (mod m)
    n = 1
    d %= m
    while n*x % m != d:
        n += 1
    return n


def part2(buses):
    # So this is basically the chinese remainder theorem
    # Common knowledge, obviously

    # compute product of all elements, which are all coprime
    total_prod = reduce(lambda x,y: x*y,
                        (b for b in buses if b is not None))

    departure_time = 0

    for i, bus in enumerate(buses):

        if bus is None:
            continue

        # compute product of all elements excluding the current element
        prod = total_prod // bus

        # now find something to multiply this product by so that it is
        # n*prod + i = 0 (mod bus)
        n = solve(prod, -i, bus)

        # now add this new term to our solution
        departure_time += n*prod

    # at this point `departure_time` is a valid solution, but a smaller one
    # mod `total_prod` may exist
    return departure_time % total_prod


def main(input_file):

    with open(input_file, 'r') as f:
        departure_time = int(f.readline())
        buses = [int(bus) if bus != 'x' else None
                 for bus in f.readline().rstrip().split(',')]

    val = part1(departure_time, buses)
    print("Part 1:", val)

    val = part2(buses)
    print("Part 2:", val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
