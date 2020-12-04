from functools import reduce


def part1(graph, slope):
    dx, dy = slope
    x, y = 0, 0
    w, h = len(graph[0]), len(graph)

    tree = '#'
    n_trees = 0

    while y + dy < h:
        x = (x + dx) % w
        y += dy
        n_trees += (graph[y][x] == tree)

    return n_trees


def part2(graph):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    collisions = (part1(graph, slope) for slope in slopes)
    return reduce(lambda x,y: x*y, collisions)


def main():
    with open('input.txt', 'r') as f:
        graph = [l.strip() for l in f.readlines()]
    n_trees = part1(graph, (3, 1))
    print("Part 1:", n_trees)
    res = part2(graph)
    print("Part 2:", res)


if __name__ == '__main__':
    main()
