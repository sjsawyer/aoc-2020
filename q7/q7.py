import re
import sys


def part1(rules):
    '''
    Our goal is to find out how many colors eventually lead to a
    'shiny gold' bag. We can start at each color and see if it leads to
    a shiny goal bag, keeping track of all other colors along the way to
    avoid recomputing these subproblems.
    '''

    # Store whether or not we can reach our goal from a particular bag
    dp = {color: None for color in rules}

    goal = 'shiny gold'
    dp[goal] = False

    def can_reach_goal(node):
        if dp[node] is not None:
            # We've calculated this already
            return dp[node]
        if goal in rules[node]:
            # The goal is our neighbour
            return True
        # Check if we can reach the goal from any of our neighbours
        for nbr in rules[node]:
            if can_reach_goal(nbr):
                dp[node] = True
                return True
        # We did not reach the goal
        dp[node] = False
        return False

    return sum(can_reach_goal(color) for color in rules)


def part2(rules):
    # total number of bags contained by a given bag color
    dp = {color: None for color in rules}

    def number_of_bags_from_here(node):
        if dp[node] is not None:
            return dp[node]

        bags_from_here = 0
        for nbr in rules[node]:
            bags_contained_by_nbr = number_of_bags_from_here(nbr)
            # This is num of neighbours of one particular bag color
            n_nbrs = rules[node][nbr]
            bags_from_here += (n_nbrs + n_nbrs*bags_contained_by_nbr)

        dp[node] = bags_from_here
        return bags_from_here

    return number_of_bags_from_here('shiny gold')


def parse_input(infile):
    color_reg = re.compile('^(.+) bags contain (.+)\.$')
    contents_reg = re.compile('(\d+) (.+) bags?')
    rules = {}
    with open(infile, 'r') as f:
        line = f.readline().rstrip()
        while line:
            color, remaining = color_reg.match(line).groups()
            rules[color] = {}
            if 'no other' in remaining:
                pass
            else:
                bags = remaining.split(', ')
                for bag in bags:
                    n, c = contents_reg.match(bag).groups()
                    rules[color][c] = int(n)
            line = f.readline().rstrip()
    return rules



def main(input_file):
    rules = parse_input(input_file)
    n_bags = part1(rules)
    print("Part 1:", n_bags)

    n_bags = part2(rules)
    print("Part 2:", n_bags)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
