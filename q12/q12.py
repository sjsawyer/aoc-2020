import sys

heading_order = ['N', 'E', 'S', 'W']

heading_to_delta = {
    'N': [0, 1],
    'E': [1, 0],
    'S': [0, -1],
    'W': [-1, 0]
}


def rotate(a, n, heading):
    n_rotations = n // 90
    if a == 'R':
        # rotate right
        idx = heading_order.index(heading)
        new_idx = (idx + n_rotations) % 4
        new_heading = heading_order[new_idx]
        return new_heading
    return rotate('R', -n, heading)


def part1(actions):
    heading = 'E'
    pos = [0, 0]

    for action in actions:
        a, n = action
        if a in heading_to_delta:
            dx, dy = heading_to_delta[a]
            pos[0] += dx*n
            pos[1] += dy*n
        elif a == 'F':
            # move in direction of current heading
            dx, dy = heading_to_delta[heading]
            pos[0] += dx*n
            pos[1] += dy*n
        elif a == 'R' or a == 'L':
            heading = rotate(a, n, heading)
        else:
            raise Exception('invalid action')

    return abs(pos[0]) + abs(pos[1])


def rotate_waypoint(waypoint, n, a):
    n_rotations = n // 90
    x, y = waypoint
    if a == 'R':
        # rotate clockwise
        for _ in range(n_rotations):
            x, y = y, -x
    elif a == 'L':
        # rotate counter-clockwise
        for _ in range(n_rotations):
            x, y = -y, x
    return [x, y]


def part2(actions):
    heading = 'E'
    pos = [0, 0]
    waypoint = [10, 1]

    for action in actions:
        a, n = action
        if a in heading_to_delta:
            dx, dy = heading_to_delta[a]
            waypoint[0] += dx*n
            waypoint[1] += dy*n
        elif a == 'F':
            # move in direction of waypoint
            pos[0] += waypoint[0]*n
            pos[1] += waypoint[1]*n
        elif a == 'R' or a == 'L':
            waypoint = rotate_waypoint(waypoint, n, a)
        else:
            raise Exception('invalid action')

    return abs(pos[0]) + abs(pos[1])


def main(input_file):

    with open(input_file, 'r') as f:
        data = [l.rstrip() for l in f.readlines()]
    actions = [(e[0], int(e[1:])) for e in data]

    val = part1(actions)
    print('Part 1:', val)

    val = part2(actions)
    print('Part 2:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
