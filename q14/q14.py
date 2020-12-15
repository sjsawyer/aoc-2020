import re
import sys


def part1(program):

    def update_val(val, mask):
        # first set the bits we are updating in val to zero
        mod_mask = int(mask.replace('1', '0').replace('X', '1'), 2)
        val &= mod_mask
        # now add in the 1's of the mask
        val += int(mask.replace('X', '0'), 2)
        return val

    memory = {}
    mask = None
    for step in program:

        if step[0] == 'mask':
            mask = step[1]
            continue

        address, val = step[1:]
        address, val = int(address), int(val)
        memory[address] = update_val(val, mask)

    return sum(memory.values())


def part2(program):

    def gen_memory_addresses(address, mask):
        # Alright string manipulation it is
        address = list(bin(int(address))[2:])
        # pad address
        address = ['0'] * (36 - len(address)) + address

        one_idxs = [i for i in range(len(mask)) if mask[i] == '1']
        for idx in one_idxs:
            address[idx] = '1'

        floating_idxs = [i for i in range(len(mask)) if mask[i] == 'X']
        for b in range(1 << len(floating_idxs)):
            # convert to binary and pad with zeros
            bits = bin(b)[2:].zfill(len(floating_idxs))
            for idx, bit in zip(floating_idxs, bits):
                address[idx] = bit
            yield int(''.join(address), 2)

    memory = {}
    mask = None
    for step in program:

        if step[0] == 'mask':
            mask = step[1]
            continue

        address, val = step[1:]
        address, val = int(address), int(val)
        # keep address as a string for now
        for new_address in gen_memory_addresses(address, mask):
            memory[new_address] = val

    return sum(memory.values())


def main(input_file):
    mask_reg = re.compile(r'(mask) = ([01X]+)')
    mem_reg = re.compile(r'^(mem)\[(\d+)\] = (\d+)')
    program = []
    with open(input_file, 'r') as f:
        line = f.readline()
        while line:
            match = mask_reg.match(line) or mem_reg.match(line)
            program.append(match.groups())
            line = f.readline()

    res = part1(program)
    print("Part 1:", res)

    res = part2(program)
    print("Part 2:", res)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
