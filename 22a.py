from collections import deque 

# Get input
with open('./inp/22.txt') as f:
    p1, p2 = [deque(map(int, i.split('\n')[1:])) for i in f.read().split('\n\n')]

while len(p1) > 0 and len(p2) > 0:
    c1, c2 = p1.popleft(), p2.popleft()
    if c1 > c2: p1.append(c1);p1.append(c2)
    elif c1 < c2: p2.append(c2);p2.append(c1)
winner = p1 if len(p1) > 0 else p2

score = sum([winner.pop() * i for i in range(1, len(winner) + 1)])
print(score)
