import re
from collections import defaultdict

def find_gold(start):
    if len(mappings[start]) == 0:
        return False

    if 'shiny gold' in mappings[start]:
        return True

    return any(find_gold(i) for i in mappings[start])

mappings = defaultdict(lambda: set())

with open('./inp/07.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

for rule in inp:
    outer, inners = re.match(r'(\w+\s\w+) bags contain ([\w\s,]+)', rule).groups()
    inners = inners.split(', ')
    for inner in inners:

        # parse the string
        amount, color = inner.split(' ', 1)
        if amount == 'no': continue
        amount = int(amount) # int digit of how many
        color = " ".join(color.split(' ', 2)[:-1]) # strip off 'bags' so it's just the color.. in the ugliest way possible
        
        # add to mappings
        mappings[outer].add(color)

keys = list(mappings.keys())

print(sum(1 for i in keys if find_gold(i)))