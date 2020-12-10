from collections import deque

with open('./inp/10.txt') as f:
    q = deque(sorted(map(int, [line.rstrip() for line in f.readlines()])))
q.append(q[-1] + 3)
d = {1:0,3:0}

last = 0
while len(q) > 0:
    c = q.popleft()
    diff = c - last
    if diff in d:
        d[diff] += 1
    last = c
print(d[1] * d[3])