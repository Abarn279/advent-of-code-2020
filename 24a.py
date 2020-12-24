from collections import defaultdict, deque
from aoc_utils import Vector3

with open('./inp/24.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

grid = defaultdict(lambda: False)

diags = {'nw': Vector3(-1, 0, 1), 'ne': Vector3(0, -1, 1), 'se': Vector3(1, 0, -1), 'sw': Vector3(0, 1, -1)}
left_right = {'e': Vector3(1, -1, 0), 'w': Vector3(-1, 1, 0)}

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

print(sum(1 for i in grid.values() if i == True))