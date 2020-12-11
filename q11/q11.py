import sys


floor = '.'
empty = 'L'
occupied = '#'


def get_nbrs_1(grid, x, y):
    nbrs = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (0 <= i < len(grid[0])
                    and 0 <= j < len(grid)
                    and (x, y) != (i, j)):
                nbrs.append(grid[j][i])
    return nbrs


def get_nbrs_2(grid, x, y):
    nbrs = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):

            if (dx, dy) == (0, 0):
                continue

            i, j = x + dx, y + dy
            while True:
                if i < 0 or j < 0 or i == len(grid[0]) or j == len(grid):
                    break
                if grid[j][i] != floor:
                    nbrs.append(grid[j][i])
                    break
                else:
                    i += dx
                    j += dy
    return nbrs


def get_next_state(grid, threshold, get_nbrs):
    next_state = [[None for _ in range(len(grid[0]))]
                  for _ in range(len(grid))]
    mutated = False

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == floor:
                next_state[y][x] = floor
                continue

            nbrs = get_nbrs(grid, x, y)
            if grid[y][x] == occupied and nbrs.count(occupied) >= threshold:
                next_state[y][x] = empty
                mutated = True
            elif grid[y][x] == empty and nbrs.count(occupied) == 0:
                next_state[y][x] = occupied
                mutated = True
            else:
                next_state[y][x] = grid[y][x]

    return mutated, next_state


def part1(grid):

    while True:
        mutated, next_state = get_next_state(grid, 4, get_nbrs_1)
        if not mutated:
            break
        grid = next_state

    return sum(grid[j][i] == occupied
               for j in range(len(grid))
               for i in range(len(grid[0])))


def part2(grid):

    while True:
        mutated, next_state = get_next_state(grid, 5, get_nbrs_2)

        if not mutated:
            break
        grid = next_state

    return sum(grid[j][i] == occupied
               for j in range(len(grid))
               for i in range(len(grid[0])))


def main(input_file):

    with open(input_file, 'r') as f:
        grid = [list(l.rstrip()) for l in f.readlines()]

    val = part1(grid)
    print('Part 1:', val)

    val = part2(grid)
    print('Part 2:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
