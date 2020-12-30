import sys
from functools import reduce


def part1and2(data):
    # known ingredients with allergens
    allergen_to_ingredient = {}

    # possible ingredients containing a given allergen
    candidate_ingredients = {}

    # all allergens
    all_allergens = set()
    for d in data:
        all_allergens.update(d[1])

    for allergen in all_allergens:
        candidate_ingredients[allergen] = reduce(
            lambda x, y:  x.intersection(y),
            (d[0] for d in data if allergen in d[1]))

    while len(allergen_to_ingredient) < len(all_allergens):
        # Iteratively check which ingredients are known to have allergens
        # and remove this ingredient from the candidate ingredients
        to_remove = {}
        for allergen, ingredients in candidate_ingredients.items():
            if len(ingredients) == 1:
                ingredient = next(iter(ingredients))
                allergen_to_ingredient[allergen] = ingredient
                to_remove[allergen] = ingredient
        for allergen, ingredient in to_remove.items():
            del candidate_ingredients[allergen]
            for ingredients in candidate_ingredients.values():
                if ingredient in ingredients:
                    ingredients.remove(ingredient)

    ingredient_count = {}
    for d in data:
        for e in d[0]:
            ingredient_count[e] = ingredient_count.get(e, 0) + 1

    allergenic_ingredients = allergen_to_ingredient.values()
    part1 = sum(ingredient_count[i] for i in ingredient_count
                if i not in allergenic_ingredients)

    # part 2
    ingredient_to_allergen = {v:k for k,v in allergen_to_ingredient.items()}
    part2 = ','.join(sorted(
        allergenic_ingredients,
        key=lambda ingredient: ingredient_to_allergen[ingredient]))

    return part1, part2


def main(input_file):
    with open(input_file, 'r') as f:
        content = f.read().splitlines()
    data = []
    for line in content:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split()
        allergens = allergens[:-1].split(', ')
        data.append((set(ingredients), set(allergens)))


    part1, part2 = part1and2(data)
    print('Part 1:', part1)
    print('Part 2:', part2)


if __name__ == '__main__':
    input_file = sys.argv[-1] if len(sys.argv) > 1 else 'input.txt'
    main(input_file)
