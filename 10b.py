from collections import deque, defaultdict
from py_linq import Enumerable as _

dp = {} # dynamic programming store for adapters
def get_paths(a_map, a):
    global dp

    if a in dp: # return if we've calculated for this adapter already
        return dp[a]

    if a not in a_map: # base case - we've reached the end
        return 1

    total = 0

    for child in a_map[a]: # add up the amount of child paths (and their child paths), return
        amt = get_paths(a_map, child)
        dp[child] = amt
        total += amt

    return total

with open('./inp/10.txt') as f:
    adapters = _([line.rstrip() for line in f.readlines()]) \
        .select(lambda x: int(x)) \
        .order_by(lambda x: x) \
        .to_list()

adapters.append(adapters[-1] + 3) # append "my" adapter (aka highest + 3)

a_map = defaultdict(lambda: []) # create the stored map of adapter to next possible adapters
a_map[0] = [i for i in [1, 2, 3] if i in adapters] # add choices from 0 (1, 2, 3, if they exist in input)
for i in range(len(adapters)):
    for j in range(i + 1, i + 4):
        if j < len(adapters) and adapters[j] - adapters[i] <= 3:
            a_map[adapters[i]].append(adapters[j])

print(get_paths(a_map, 0))