import sys
import re


def part1(rules, messages):
    # convert the dict to regex
    reg_map = {}
    def get_reg(rule):
        """Recursively generate the regex for a given rule"""
        if rule in reg_map:
            return reg_map[rule]
        if isinstance(rules[rule], str):
            res = rules[rule]
            reg_map[rule] = res
            return res
        regs = []
        for tup in rules[rule]:
            regs.append(r''.join(get_reg(n) for n in tup))
        res = r'|'.join(r'({})'.format(r) for r in regs)
        res = r'({})'.format(res)
        reg_map[rule] = res
        return res

    root_reg = get_reg(0)
    compiled = re.compile(root_reg)
    total_matches = 0
    for message in messages:
        match = compiled.match(message)
        if match:
            match_text = message[match.start():match.end()]
            total_matches += (match_text == message)
    return total_matches


def part2():
    pass


def main(input_file):
    patterns = [
        r'(\d+):((?: \d+)+)$',
        r'(\d+):((?: \d+)+) \|((?: \d+)+)$',
        r'(\d+): "(\w)"$',
    ]
    pattern = r'|'.join(r'({})'.format(p) for p in patterns)
    rule_reg = re.compile(pattern)

    with open(input_file, 'r') as f:
        rules, messages = f.read().split('\n\n')

    rules = [list(filter(None, rule_reg.match(line).groups()))
                 for line in rules.splitlines()]

    rule_dict = {}
    for rule in rules:
        if '"' in rule[0]:
            rule_dict[int(rule[1])] = rule[2]
        else:
            rule_dict[int(rule[1])] = [
                [int(d) for d in nums[1:].split(' ')]
                for nums in rule[2:]]

    messages = messages.splitlines()


    val = part1(rule_dict, messages)
    print("Part 1", val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
