import sys
from collections import deque
from copy import deepcopy


def calc_score(deck):
    return sum(x*y for x,y in zip(range(1, len(deck)+1), reversed(deck)))


def part1(p1, p2):
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))

    winner = p1 or p2
    return calc_score(winner)


def slice_(p1, i, j):
    # hacky slice implementation for deques
    return deque(list(p1)[i:j])


def part2(p1, p2):

    seen = set()

    while p1 and p2:

        # condition 1: state already seen
        state = (tuple(p1), tuple(p2))
        if state in seen:
            # player 1 wins
            return 1, calc_score(p1)
        seen.add(state)

        # draw
        c1, c2 = p1.popleft(), p2.popleft()

        # condition 2: enough cards, play subgame
        if len(p1) >= c1 and len(p2) >= c2:
            winner, _ = part2(slice_(p1, 0, c1), slice_(p2, 0, c2))
            if winner == 1:
                p1.extend((c1, c2))
            else:
                p2.extend((c2, c1))
        else:
            # condition 3: not enough cards, round winner and game continues
            if c1 > c2:
                p1.extend((c1, c2))
            else:
                p2.extend((c2, c1))

    # condition 4: someone has no more cards, game over
    winner, score = (1, calc_score(p1)) if p1 else (2, calc_score(p2))
    return winner, score


def main(input_file):
    with open(input_file, 'r') as f:
        p1, p2 = [l.strip() for l in f.read().split('\n\n')]
    p1 = [int(d) for d in p1.split('\n')[1:]]
    p2 = [int(d) for d in p2.split('\n')[1:]]
    p1, p2 = deque(p1), deque(p2)

    val1 = part1(deepcopy(p1), deepcopy(p2))
    print('Part 1:', val1)

    _, val2 = part2(deepcopy(p1), deepcopy(p2))
    print('Part 2:', val2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
