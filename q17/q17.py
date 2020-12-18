import sys
import copy


inactive = '.'
active = '#'


def get_nbrs_3d(grid, x, y, z):
    nbrs = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if (0 <= i < len(grid[0][0])
                        and 0 <= j < len(grid[0])
                        and 0 <= k < len(grid)
                        and (x, y, z) != (i, j, k)):
                    nbrs.append(grid[k][j][i])
    return nbrs


def get_nbrs_4d(grid, x, y, z, w):
    nbrs = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if (0 <= i < len(grid[0][0][0])
                            and 0 <= j < len(grid[0][0])
                            and 0 <= k < len(grid[0])
                            and 0 <= l < len(grid)
                            and (x, y, z, w) != (i, j, k, l)):
                        nbrs.append(grid[l][k][j][i])
    return nbrs


def get_next_state_3d(grid):
    # new dimensions for next state
    n_z = len(grid) + 2
    n_y = len(grid[0]) + 2
    n_x = len(grid[0][0]) + 2

    new_grid = [[[inactive for _ in range(n_x)]
                 for _ in range(n_y)]
                for _ in range(n_z)]

    # now we expand each slice and place them
    for z in range(len(grid)):
        for y in range(len(grid[0])):
            for x in range(len(grid[0][0])):
                new_grid[z+1][y+1][x+1] = grid[z][y][x]

    # Now generate the next state
    next_state = [[[None for _ in range(n_x)]
                   for _ in range(n_y)]
                  for _ in range(n_z)]
    for z in range(n_z):
        for y in range(n_y):
            for x in range(n_x):
                nbrs = get_nbrs_3d(new_grid, x, y, z)
                # apply update rules
                if (new_grid[z][y][x] == active
                        and not 2 <= nbrs.count(active) <= 3):
                    next_state[z][y][x] = inactive
                elif (new_grid[z][y][x] == inactive
                        and nbrs.count(active) == 3):
                    next_state[z][y][x] = active
                else:
                    next_state[z][y][x] = new_grid[z][y][x]

    return next_state


def get_next_state_4d(grid):
    # new dimensions for next state
    n_w = len(grid) + 2
    n_z = len(grid[0]) + 2
    n_y = len(grid[0][0]) + 2
    n_x = len(grid[0][0][0]) + 2

    new_grid = [[[[inactive for _ in range(n_x)]
                  for _ in range(n_y)]
                 for _ in range(n_z)]
                for _ in range(n_w)]

    # now we expand each slice and place them
    for w in range(len(grid)):
        for z in range(len(grid[0])):
            for y in range(len(grid[0][0])):
                for x in range(len(grid[0][0][0])):
                    new_grid[w+1][z+1][y+1][x+1] = grid[w][z][y][x]

    # Now generate the next state
    next_state = [[[[None for _ in range(n_x)]
                    for _ in range(n_y)]
                   for _ in range(n_z)]
                  for _ in range(n_w)]

    for w in range(n_w):
        for z in range(n_z):
            for y in range(n_y):
                for x in range(n_x):
                    nbrs = get_nbrs_4d(new_grid, x, y, z, w)
                    # apply update rules
                    if (new_grid[w][z][y][x] == active
                            and not 2 <= nbrs.count(active) <= 3):
                        next_state[w][z][y][x] = inactive
                    elif (new_grid[w][z][y][x] == inactive
                            and nbrs.count(active) == 3):
                        next_state[w][z][y][x] = active
                    else:
                        next_state[w][z][y][x] = new_grid[w][z][y][x]

    return next_state


def part1(grid):

    for _ in range(6):
        grid = get_next_state_3d(grid)

    return sum(grid[k][j][i] == active
               for k in range(len(grid))
               for j in range(len(grid[0]))
               for i in range(len(grid[0][0])))


def part2(grid):

    for _ in range(6):
        grid = get_next_state_4d(grid)

    return sum(grid[l][k][j][i] == active
               for l in range(len(grid))
               for k in range(len(grid[0]))
               for j in range(len(grid[0][0]))
               for i in range(len(grid[0][0][0])))


def main(input_file):

    with open(input_file, 'r') as f:
        grid = [[list(l.rstrip()) for l in f.readlines()]]

    val = part1(copy.deepcopy(grid))
    print('Part 1:', val)

    grid = [grid]
    val = part2(grid)
    print('Part 2:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
