import sys
import re


def get_reg(rule, reg_map, rules):
    """Recursively generate the regex for a given rule"""
    if rule in reg_map:
        return reg_map[rule]
    if isinstance(rules[rule], str):
        res = rules[rule]
        reg_map[rule] = res
        return res
    regs = []
    for tup in rules[rule]:
        regs.append(r''.join(get_reg(n, reg_map, rules) for n in tup))
    res = r'|'.join(r'({})'.format(r) for r in regs)
    res = r'({})'.format(res)
    reg_map[rule] = res
    return res


def part1(rules, messages):
    reg_map = {}
    root_reg = get_reg(0, reg_map, rules)
    compiled = re.compile(root_reg)
    return sum(bool(compiled.fullmatch(message)) for message in messages)


def part2(rules, messages):
    # First lets generate rules for 42 and 31
    reg_map = {}
    r42 = get_reg(42, reg_map, rules)
    r31 = get_reg(31, reg_map, rules)

    # now lets manually create the rules for 8 ...
    # 42
    # 42 42
    # 42 42 42
    # ...
    reg_map[8] = r'({}+)'.format(r42)

    # ... and rule 11
    # 42 31
    # 42(42 31)31
    # 42(42(42 31)31)31
    # ...
    r11 = r'({}{})'.format(r42, r31)
    for _ in range(3):
        # 3 determined from trial and error on given input
        # (anything > 3 would also work, just longer runtime)
        r11 = r'({}{}?{})'.format(r42, r11, r31)
    reg_map[11] = r11

    # the rest is the same as part 1
    root_reg = get_reg(0, reg_map, rules)
    compiled = re.compile(root_reg)
    return sum(bool(compiled.fullmatch(message)) for message in messages)


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

    val = part2(rule_dict, messages)
    print("Part 2", val)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
