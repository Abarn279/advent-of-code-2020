with open('./inp/03.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

grid = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[(x, y)] = inp[y][x]
        
max_x = len(inp[0])
pos = (0, 0)
trees = 0
while pos[0] < len(inp):
    pos = ((pos[0] + 3) % max_x, pos[1] + 1)

    if pos not in grid:
        break

    if grid[pos] == '#': trees += 1
print(trees)