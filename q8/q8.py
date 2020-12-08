import sys


def part1(program):
    acc = 0
    visited = set()
    i = 0
    while i not in visited:
        visited.add(i)
        instruction, value = program[i]
        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            acc += value
            i += 1
        elif instruction == 'jmp':
            i += value
        else:
            raise ValueError(f'Invalid instruction "{instruction}"')

    return acc


def part2(program):

    def run(program):
        ''' Essentially part 1 with a few tweaks '''
        terminates = False
        acc = 0
        visited = set()
        i = 0

        while i not in visited:
            if i == len(program):
                terminates = True
                break

            visited.add(i)
            instruction, value = program[i]
            if instruction == 'nop':
                i += 1
            elif instruction == 'acc':
                acc += value
                i += 1
            elif instruction == 'jmp':
                i += value
            else:
                raise ValueError(f'Invalid instruction "{instruction}"')

        return terminates, acc

    for j in range(len(program)):
        prev = program[j]
        instruction, value = prev
        if instruction == 'jmp':
            program[j] = ('nop', value)
        elif instruction == 'nop':
            program[j] == ('jmp', value)
        terminates, acc = run(program)
        if terminates:
            return acc
        program[j] = prev

    raise RuntimeError('Program never terminates')


def main(input_file):

    with open(input_file, 'r') as f:
        program = []
        for l in f.readlines():
            instruction, value = l.rstrip().split()
            program.append((instruction, int(value)))

    val = part1(program)
    print('Part 1:', val)

    val = part2(program)
    print('Part 2:', val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
