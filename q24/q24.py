import sys

DIR_TO_COORD = {
    'e': (2, 0),
    'w': (-2, 0),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1),
}


def part1(tiles):
    # store number of times we see each tile
    coords = {}
    for tile in tiles:
        tile_coords = [DIR_TO_COORD[d] for d in tile]
        res = (sum(c[0] for c in tile_coords), sum(c[1] for c in tile_coords))
        coords[res] = coords.get(res, 0) + 1

    # black tiles flipped an odd number of times
    black = {c: v for c,v in coords.items() if v % 2 == 1}
    return black


def get_nbrs(coord, _nbrs={}):
    # Store neighbours to avoid recomputing. Unnecessary, but minor speedup
    if coord in _nbrs:
        return _nbrs[coord]
    nbrs = {(coord[0] + c[0], coord[1] + c[1])
            for c in DIR_TO_COORD.values()}
    _nbrs[coord] = nbrs
    return nbrs


def part2(blacks):
    blacks = set(blacks.keys())

    for _ in range(100):
        next_blacks = set()
        whites = set()
        # update black cells and get adjacent white cells
        for black in blacks:
            nbrs = get_nbrs(black)
            black_nbrs = blacks.intersection(nbrs)
            whites.update(nbrs.difference(black_nbrs))
            # if this tile stays black, keep it for next iteration
            if 0 < len(black_nbrs) < 3:
                next_blacks.add(black)
        # update white cells
        for white in whites:
            if len(blacks.intersection(get_nbrs(white))) == 2:
                # this white tile flips to black next iteration
                next_blacks.add(white)

        blacks = next_blacks

    return len(blacks)


def main(input_file):
    with open(input_file, 'r') as f:
        content = f.read().splitlines()
    tiles = []
    for s in content:
        tile, i = [], 0
        while i < len(s):
            if s[i] in {'n', 's'}:
                tile.append(s[i:i+2])
                i += 2
            else:
                tile.append(s[i])
                i += 1
        tiles.append(tile)

    blacks = part1(tiles)
    print('Part 1:', len(blacks))

    n_blacks = part2(blacks)
    print('Part 2:', n_blacks)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
