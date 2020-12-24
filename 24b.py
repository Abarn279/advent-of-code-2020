from collections import defaultdict, deque
from aoc_utils import Vector3

with open('./inp/24.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

grid = defaultdict(lambda: False)

diags = {'nw': Vector3(-1, 0, 1), 'ne': Vector3(0, -1, 1), 'se': Vector3(1, 0, -1), 'sw': Vector3(0, 1, -1)}
left_right = {'e': Vector3(1, -1, 0), 'w': Vector3(-1, 1, 0)}
all_directions = {**diags, **left_right}

# Build initial grid
for line in inp:
    delta = Vector3(0, 0, 0)

    q = deque(line)
    while len(q) > 0:

        found_two = True
        # try for 2
        if len(q) > 1:
            d = q.popleft() + q.popleft()

            if d in diags:
                delta += diags[d]
            else:
                q.appendleft(d[1]);q.appendleft(d[0])
                found_two = False
        
        if len(q) == 1 or not found_two:
            d = q.popleft()
            delta += left_right[d]

    grid[delta] = not grid[delta]

# Part 1
print(sum(1 for i in grid.values() if i == True))

for day in range(100):

    # LORD JESUS FORGIVE ME
    ks = list(grid.keys())
    for k in ks:
        for d in all_directions:
            grid[k + all_directions[d]]

    # ok now go do the real calculation
    new_grid = defaultdict(lambda: False)
    items = list(grid.items())
    for k, v in items:
        num_adjacent = sum(1 for d in all_directions if grid[k + all_directions[d]] == True)
        if v and (num_adjacent == 0 or num_adjacent > 2): 
            new_grid[k] = False
        elif not v and (num_adjacent == 2): 
            new_grid[k] = True
        else: 
            new_grid[k] = grid[k]
    grid = new_grid

# Part 2
print(sum(1 for i in grid.values() if i == True))