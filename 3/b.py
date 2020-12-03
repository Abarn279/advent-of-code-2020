def product(ary):
    prod = ary[0]
    for i in range(1, len(ary)):
        prod *= ary[i]
    return prod

with open('./3.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

def get_trees(x, y):
    global grid
    global max_x

    pos = (0, 0)
    trees = 0
    while pos[0] < len(inp):
        pos = ((pos[0] + x) % max_x, pos[1] + y)

        if pos not in grid:
            break

        if grid[pos] == '#': trees += 1
    return trees

grid = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[(x, y)] = inp[y][x]
max_x = len(inp[0])

print(product([get_trees(*x) for x in [(1, 1), (3,1), (5,1), (7,1), (1, 2)]]))