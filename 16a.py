import re
import math
from collections import deque

class Field:
    def __init__(self, string):
        name, a, b, c, d = re.match(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', string).groups()
        self.name = name
        self.lowrange = set(range(int(a), int(b)+1))
        self.highrange = set(range(int(c), int(d)+1))
    def __contains__(self, key):
        return key in self.lowrange or key in self.highrange

# Define if a ticket is valid
def is_valid(nt):
    data = list(map(int, nt.split(',')))
    for datum in data:
        if not any(True for field in fields if datum in field): 
            return False
    return True

# Get and parse input
with open('./inp/16.txt') as f:
    fields, your_ticket, nearby_tickets = f.read().split("\n\n")
fields = [Field(i) for i in fields.split('\n')]
your_ticket = your_ticket.split('\n')[1]
nearby_tickets = nearby_tickets.split('\n')[1:]

# Filter out invalid tickets
nearby_tickets = [i for i in nearby_tickets if is_valid(i)]

# Track the possible fields for each index
possible_fieldnames_for_index = {}
for i in range(len(your_ticket.split(','))): 
    all_fields = {f.name: f for f in fields}
    removed = set()

    for nt in nearby_tickets:
        val = int(nt.split(',')[i])

        for field in all_fields.keys():
            if val not in all_fields[field]:
                removed.add(field)
        
    possible_fieldnames_for_index[i] = set(all_fields.keys()).difference(removed)
    
# Solve so that there's only one field for each
q = deque(possible_fieldnames_for_index)
while len(q) > 0:
    ind = q.popleft()

    length = len(possible_fieldnames_for_index[ind])

    # if there's only 1 possible fieldname, then go remove it from all the others
    if length == 1:
        single_fieldname = min(possible_fieldnames_for_index[ind]) # used min to extract a single value
        for other_ind in q:
            possible_fieldnames_for_index[other_ind].remove(single_fieldname)

    # if there's more than one possible, just visit this one later.
    elif length > 1:
        q.append(ind)

print(math.prod([int(your_ticket.split(',')[i]) for i in possible_fieldnames_for_index if min(possible_fieldnames_for_index[i]).startswith('departure')]))
