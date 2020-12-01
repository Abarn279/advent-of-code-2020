import itertools

def do_sol(inp):
    combos = itertools.combinations(inp, 3)

    for c in combos:
        if sum(c) == 2020:
            return c[0] * c[1] * c[2]

with open('./1.txt') as f:
    inp = list(map(int, [line.rstrip() for line in f.readlines()]))

print(do_sol(inp))

