import sys
import operator
from collections import deque
from functools import reduce


def evaluate(expression):
    prev_op = lambda _, y: y
    res = None

    while expression:
        n = expression.popleft()
        if n == ')':
            return res
        elif n == '(':
            res = prev_op(res, evaluate(expression))
        elif n == '*':
            prev_op = operator.mul
        elif n == '+':
            prev_op = operator.add
        else:
            res = prev_op(res, int(n))

    return res


def evaluate_2(expression):
    prev_op = None
    to_mult = []

    while expression:
        n = expression.popleft()
        if n == ')':
            break
        elif n == '*':
            prev_op = operator.mul
        elif n == '+':
            prev_op = operator.add
        elif n == '(' and prev_op == operator.add:
            to_mult[-1] += evaluate_2(expression)
        elif n == '(':
            to_mult.append(evaluate_2(expression))
        elif prev_op == operator.add:
            to_mult[-1] += int(n)
        else:
            to_mult.append(int(n))

    return reduce(lambda x,y: x*y, to_mult)


def part1(homework):
    return sum(evaluate(deque(expression)) for expression in homework)


def part2(homework):
    return sum(evaluate_2(deque(expression)) for expression in homework)


def main(input_file):

    with open(input_file, 'r') as f:
        homework = [l.rstrip().replace(' ', '')  for l in f.readlines()]

    val = part1(homework)
    print("Part 1", val)

    val = part2(homework)
    print("Part 2", val)



if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
