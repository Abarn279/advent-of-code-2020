import re
from collections import defaultdict, deque

class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens
    def __repr__(self):
        return f"{' '.join(self.ingredients)} (contains {', '.join(self.allergens)})"

def remove_ingredient_and_allergen(foods, ingredient, allergen):
     for f in foods:
        if allergen in f.allergens: f.allergens.remove(allergen)
        if ingredient in f.ingredients: f.ingredients.remove(ingredient)

# Get input
with open('./inp/21.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

foods = []

# input => list of foods
for line in inp: 
    i, a = re.match(r'([\w\s]+) \(contains ([\w\s\,]+)\)', line).groups()
    i = set(i.split(' '))
    a = set(a.split(', '))
    foods.append(Food(i, a))

all_allergens = set([i for f in foods for i in f.allergens])

# A queue of all foods which i'll cycle through. My usual garbage circular solving technique.
allergens = deque(all_allergens)

# map of ingredient name (gibberish) to the single allergen it must represent.
ingredients_to_allergens = {}

# While we haven't solved all allergens...
while len(ingredients_to_allergens) < len(all_allergens):

    allergen = allergens.popleft()

    foods_containing_aller = [f for f in foods if allergen in f.allergens]

    # if ingredients / allergens are 1:1 it's solved
    if len(foods_containing_aller) == 1:
        if len(foods_containing_aller[0].ingredients) == len(foods_containing_aller[0].allergens):
            ingredients_to_allergens[list(foods_containing_aller[0].ingredients)[0]] = allergen
            remove_ingredient_and_allergen(foods, list(foods_containing_aller[0].ingredients)[0], allergen)

            # since this food is completely solved, don't append it back onto the queue
            continue
    
    else:
        ingredients_set = foods_containing_aller[0].ingredients.copy()
        for fca in foods_containing_aller:
            ingredients_set = ingredients_set.intersection(fca.ingredients)

        if len(ingredients_set) == 1:
            ingredients_to_allergens[max(ingredients_set)] = allergen
            remove_ingredient_and_allergen(foods, max(ingredients_set), allergen)
            continue

    # cycle allergens
    allergens.append(allergen)

# A pure flattened list of all ingredients seen (including duplicates)
all_uses = [i for f in foods for i in f.ingredients]

# non-allergenic ingredients
non_allergen = set(all_uses) - set(ingredients_to_allergens.keys())

# part A
print(sum(1 for i in all_uses if i in non_allergen))

# part B
print(','.join(map(lambda t: t[0],sorted(ingredients_to_allergens.items(), key = lambda x: x[1]))))