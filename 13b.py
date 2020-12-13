import math
from collections import deque

def lcm(a, b): 
    ''' best way to LCM found on stackoverflow. numpy.lcm didnt work for me since it's implemented in C using ints. '''
    return abs(a*b) // math.gcd(a, b)

with open('./inp/13.txt') as f:
    start = int(f.readline())
    bus_ids = deque(i for i in enumerate(f.readline().split(',')) if i[1] != 'x') # (Bus ID, offset)
    for i in range(len(bus_ids)): bus_ids[i] = (bus_ids[i][0], int(bus_ids[i][1]))

delta = bus_ids.popleft()[1]
nxt = bus_ids.popleft()
time = 0
while True:
    time_to_check = time + nxt[0]

    if time_to_check % nxt[1] == 0:
        delta = lcm(delta, nxt[1])

        if len(bus_ids) == 0: 
            break

        nxt = bus_ids.popleft()

    time += delta

print(time)