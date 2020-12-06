import sys
from functools import reduce


def part1_functional(groups):
    # x is total set of unique answers for the group, and y is the
    # list of answers for an individual person
    return sum(len(reduce(lambda x,y: x.union(set(y)), group, set()))
               for group in groups)


def part1(groups):
    '''
    For each group count the total number of questions for which ANYONE
    answered yes.
    '''
    total_answers = 0
    for group in groups:
        group_answers = set()
        for answers in group:
            group_answers.update(set(answers))
        total_answers += len(group_answers)
    return total_answers


def part2(groups):
    '''
    For each group count the total number of questions for which EVERYONE
    answered yes.

    For this question we will take a different approach and use bit logic.
    Since we know all answers will be from a-z, we can represent all answers
    from an individual using 26 bits. Then, to find which answers _all_ members
    had in common, we can simply 'AND' together (bitwise) all the answers and
    sum the bits which are remaining.

    E.g. 'abc', 'bcf' and 'bc' would be

    (fedcba)
    '000111'
    '100110'
    '000110'
    -------- (bitwise &)
    '000110'

    thus all answers had 2 in common, b and c.

    '''
    def string_to_bits(s):
        bits = 0
        for letter in s:
            bits |= 1 << (ord(letter) - ord('a'))
        return bits

    def total_set_bits(n):
        # could just use bin(n).count('1') but lets keep things consistent
        return sum((n >> i) & 1 for i in range(26))

    total = 0

    for group in groups:
        # initialize with all bits turned on
        common_answers = (1 << 26) - 1

        for answers in group:
            # initialize this person's answers with all bits off
            answers_as_bits = 0
            for answer in answers:
                answers_as_bits |= string_to_bits(answer)

            # Now for this group, keep only the bits (answers) which we already
            # have seen
            common_answers &= answers_as_bits

        total_in_common_for_group = total_set_bits(common_answers)
        total += total_in_common_for_group

    return total


def main(input_file):
    with open(input_file, 'r') as f:
        groups = [group.rstrip().split('\n')
                  for group in f.read().split('\n\n')]

    total_1 = part1(groups)
    print("Part 1:", total_1)

    total_2 = part2(groups)
    print("Part 2:", total_2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
