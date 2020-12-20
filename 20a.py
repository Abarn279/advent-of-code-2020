from math import sqrt, prod
from numpy import rot90, flip
from collections import deque

def are_neighbors(grid, other_grid):
    if [y[0] for y in grid] == [y[9] for y in other_grid] or \
        [y[9] for y in grid] == [y[0] for y in other_grid] or \
        grid[0] == other_grid[9] or \
        grid[9] == other_grid[0]:
        return True
    return False

def get_grid_orientations(grid):
    orientations = []

    rotated = grid[:]
    for i in range(4):
        rotated = rot90(rotated)
        flipped = flip(rotated, 1)
        orientations.append(rotated)
        orientations.append(flipped)
    
    return [i.tolist() for i in orientations]

# get input
with open('./inp/20.txt') as f:
    grid_strings = [i.split('\n') for i in f.read().split('\n\n')]
    for g in grid_strings: g[0] = g[0].split(' ')[1][:-1]
    grids = {i[0]: get_grid_orientations([list(j) for j in i[1:]]) for i in grid_strings}
    width = int(sqrt(len(grid_strings)))

corner_ids = []
for grid_key in grids:
    grid_orientation = grids[grid_key]
    other_grid_orientations_list = [grids[k] for k in grids if k != grid_key]
    
    count = 0
    grid_o = grid_orientation[0]
    for other_grid_orientation_list in other_grid_orientations_list:
        for other_grid_o in other_grid_orientation_list:
            if are_neighbors(grid_o, other_grid_o):
                count += 1
                break
    if count == 2:
        corner_ids.append(grid_key)

print(prod(map(int, corner_ids)))