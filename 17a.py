from collections import defaultdict
from aoc_utils import Vector3

def print_grid(grid): 
    for z in range(min(grid.keys(), key=lambda x: x.z).z, max(grid.keys(), key=lambda x: x.z).z + 1):
        print(f'z = {z}')
        for y in range(min(grid.keys(), key=lambda x: x.y).y, max(grid.keys(), key=lambda x: x.y).y + 1):
            for x in range(min(grid.keys(), key=lambda x: x.x).x, max(grid.keys(), key=lambda x: x.x).x + 1):
                print(grid[Vector3(x, y, z)], end="")
            print()
        print()


def get_active_neighbors(grid, pos):
    ''' Get all active neighbors in the grid for a given point '''
    return sum(1 for d in DIRECTIONS if grid[pos + d] == '#')

# Input, all 3d directions
with open('./inp/17.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

# Setup
DIRECTIONS = [Vector3(x, y, z) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1] if x != 0 or y != 0 or z != 0]
grid3d = defaultdict(lambda: '.')
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid3d[Vector3(x, y, 1)] = inp[y][x]
for z in [0, 2]:
    for y in [0, 1, 2]:
        for x in [0, 1, 2]:
            grid3d[Vector3(x, y, z)] = '.'

print_grid(grid3d)

# Run cycles
for cycle in range(6):
    copy_grid = defaultdict(lambda: '.')

    minz, maxz = min(grid3d.keys(), key=lambda x: x.z).z - 1, max(grid3d.keys(), key=lambda x: x.z).z + 2
    miny, maxy = min(grid3d.keys(), key=lambda x: x.y).y - 1, max(grid3d.keys(), key=lambda x: x.y).y + 2
    minx, maxx = min(grid3d.keys(), key=lambda x: x.x).x - 1, max(grid3d.keys(), key=lambda x: x.x).x + 2

    for z in range(minz, maxz):
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                pos = Vector3(x, y, z)
                state = grid3d[pos]
                if state == '#':
                    copy_grid[pos] = '#' if get_active_neighbors(grid3d, pos) in [2, 3] else '.'
                elif state == '.':
                    copy_grid[pos] = '#' if get_active_neighbors(grid3d, pos) == 3 else '.'

    grid3d = copy_grid
    # print(f'------------------------------------------\nAfter {str(cycle + 1)} cycles:\n')
    # print_grid(grid3d)

print(sum(1 for i in grid3d.values() if i == '#'))
