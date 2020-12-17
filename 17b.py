from collections import defaultdict
from aoc_utils import Vector4

def get_active_neighbors(grid, pos):
    ''' Get all active neighbors in the grid for a given point '''
    return sum(1 for d in DIRECTIONS if grid[pos + d] == '#')

# Input, all 3d directions
with open('./inp/17.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

# Setup
DIRECTIONS = [Vector4(x, y, z, w) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1] for w in [-1, 0, 1] if x != 0 or y != 0 or z != 0 or w != 0]
grid4d = defaultdict(lambda: '.')
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid4d[Vector4(x, y, 1, 1)] = inp[y][x]
for z in [0, 2]:
    for w in [0, 2]:
        for y in [0, 1, 2]:
            for x in [0, 1, 2]:
                    grid4d[Vector4(x, y, z, w)] = '.'

# Run cycles
for cycle in range(6):
    copy_grid = defaultdict(lambda: '.')

    minz, maxz = min(grid4d.keys(), key=lambda x: x.z).z - 1, max(grid4d.keys(), key=lambda x: x.z).z + 2
    miny, maxy = min(grid4d.keys(), key=lambda x: x.y).y - 1, max(grid4d.keys(), key=lambda x: x.y).y + 2
    minx, maxx = min(grid4d.keys(), key=lambda x: x.x).x - 1, max(grid4d.keys(), key=lambda x: x.x).x + 2
    minw, maxw = min(grid4d.keys(), key=lambda x: x.t).t - 1, max(grid4d.keys(), key=lambda x: x.t).t + 2

    for z in range(minz, maxz):
        for w in range(minw, maxw):
            for y in range(miny, maxy):
                for x in range(minx, maxx):
                    pos = Vector4(x, y, z, w)
                    state = grid4d[pos]
                    if state == '#':
                        copy_grid[pos] = '#' if get_active_neighbors(grid4d, pos) in [2, 3] else '.'
                    elif state == '.':
                        copy_grid[pos] = '#' if get_active_neighbors(grid4d, pos) == 3 else '.'

    grid4d = copy_grid

print(sum(1 for i in grid4d.values() if i == '#'))
