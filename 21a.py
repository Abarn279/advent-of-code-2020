import re
from collections import defaultdict, deque

class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens
    def __repr__(self):
        return f"{' '.join(self.ingredients)} (contains {', '.join(self.allergens)})"

# Get input
with open('./inp/21.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

# map of ingredient name (gibberish) to the single allergen it must represent.
ingredients_to_allergens = {}

# A queue of all foods which i'll cycle through. My usual garbage circular solving technique.
foods = deque()

# Get list of Food objects from input
for line in inp: 
    ingredients, allergens = re.match(r'([\w\s]+) \(contains ([\w\s\,]+)\)', line).groups()
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens.split(', '))
    foods.append(Food(ingredients, allergens))

# number of total unique allergens found within the allergens
num_allergens = len(set(a for f in foods for a in f.allergens))

# A pure flattened list of all ingredients seen (including duplicates)
all_uses = [i for f in foods for i in f.ingredients]

# While we haven't solved all allergens...
while len(ingredients_to_allergens) < num_allergens:

    # pop a food off the queue, other_foods is all foods that aren't this one
    food, other_foods = foods.popleft(), list(foods)

    # If this food has 1 allergen, then go and do a set intersect with ITS ingredient list vs. the other foods ones.
    if len(food.allergens) == 1:

        # If there's 1 allergen remaining and it's the single ingredient, we've solved this allergen. 
        if len(food.allergens) == len(food.ingredients) == 1:
            ingredients_to_allergens[max(food.ingredients)] = max(food.allergens)
            continue

        # equivalent to .Single()
        allergen = max(food.allergens)

        # for each other food...
        for of in other_foods:

            # If the allergen in our current food is IN the other list, try a set intersection
            if allergen in of.allergens:

                # get the ingredient for this allergen from the set intersection 
                matching_ingredient = food.ingredients.intersection(of.ingredients)

                if len(matching_ingredient) != 1: continue
                matching_ingredient = max(matching_ingredient)

                # keep track that this ingredient must be the current allergen
                ingredients_to_allergens[matching_ingredient] = allergen

                # now that allergen has been found, remove from all others (it's been solved!)
                food.allergens.remove(allergen)
                food.ingredients.remove(matching_ingredient)
                for of_f in other_foods:
                    if allergen in of_f.allergens: of_f.allergens.remove(allergen)
                    if matching_ingredient in of_f.ingredients: of_f.ingredients.remove(matching_ingredient)

                break

    # cycle foods
    foods.append(food)

# unique version of 'all_uses'
all_ingredients_distinct = set(all_uses)

# non-allergenic ingredients
non_allergen = all_ingredients_distinct - set(ingredients_to_allergens.keys())

print(sum(1 for i in all_uses if i in non_allergen))