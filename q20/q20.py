import re
import sys
from functools import reduce

BIT_LEN = 10


def flip(d):
    # For example 36 = 0000100100 could become 144 = 0010010000
    return int(bin(d)[2:].zfill(BIT_LEN)[::-1], 2)


def to_decimal(row):
    return int(''.join('1' if c == '#' else '0' for c in row), 2)


def flip_v(sides):
    n, e, s, w = sides
    return (s, flip(e), n, flip(w))


def flip_h(sides):
    n, e, s, w = sides
    return (flip(n), w, flip(s), e)


def rotate_cw(sides):
    n, e, s, w = sides
    return (flip(w), n, flip(e), s)


def get_rotations(sides):
    rotations = [sides]
    for _ in range(3):
        sides = rotate_cw(sides)
        rotations.append(sides)
    return rotations


def get_combinations(sides):
    # probably overkill but covers everything
    combos = set([sides])
    for rot in get_rotations(sides):
        combos.add(rot)
    sides = flip_h(sides)
    for rot in get_rotations(sides):
        combos.add(rot)
    sides = flip_v(sides)
    for rot in get_rotations(sides):
        combos.add(rot)
    return combos


def get_all_possible_sides(sides):
    return set((e for comb in get_combinations(sides) for e in comb))


def part1(tiles):
    # We will consider each tile to be a tuple of 4 numbers, 1 number for
    # each side (and direction is important!)
    # The side of a given tile will be a binary number of length 10, with
    # `#`'s being 1s and `.`'s being 0s
    # The positive directions will be down and right (so when we flip a tile
    # for example, the directions of 2 sides will be flipped, and the
    # binary number will hence also flip.
    # For example 36 = 0000100100 could become 144 = 0010010000

    bins = {}
    for tile_id, tile in tiles.items():
        n, e, s, w = (
            to_decimal(tile[0]),
            to_decimal(row[-1] for row in tile),
            to_decimal(tile[-1]),
            to_decimal(row[0] for row in tile),
        )
        bins[tile_id] = (n, e, s, w)

    combos = {}
    for n, sides in bins.items():
        combos[n] = get_combinations(sides)

    all_sides = {}
    for n, sides in bins.items():
        all_sides[n] = get_all_possible_sides(sides)

    corners = []
    for n, cs in combos.items():
        for c in cs:
            other_sides = (all_sides[m] for m in all_sides if m != n)
            res = set()
            for s in other_sides:
                res.update(s)
            matched_sides = set(c).intersection(res)
            if len(matched_sides) > 2:
                break
        else:
            # This is a sufficient condition for a corner
            corners.append(n)

    return reduce(lambda x,y: x*y, corners)


def part2():
    return None


def main(input_file):
    with open(input_file, 'r') as f:
        content = f.read().split('\n\n')

    tiles = {}
    for c in content:
        lines = c.splitlines()
        n = int(re.match('Tile (\d+):', lines[0]).groups()[0])
        tile = lines[1:]
        tiles[n] = tile

    val = part1(tiles)
    print('Part 1:', val)

    val = part2()
    print('Part 1:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
