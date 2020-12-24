from math import sqrt, prod
from numpy import rot90, flip, concatenate, array
from collections import defaultdict
from itertools import permutations
from searches import astar

def are_neighbors(grid, other_grid):
    ''' 0 is neighbor to right, 1 is top, etc '''
    if [y[9] for y in grid] == [y[0] for y in other_grid]:
        return (True, 0)
    if [y[0] for y in grid] == [y[9] for y in other_grid]:
        return (True, 2)
    if grid[9] == other_grid[0]:
        return (True, 3)
    if grid[0] == other_grid[9]:
        return (True, 1)
    
    return (False, -1)

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
    num_tiles = len(grid_strings)
    width = int(sqrt(num_tiles))

possible_connections = defaultdict(lambda: [])

# find all connections from a tile to another tile
for grid_key in grids:
    grid_orientation = grids[grid_key]
    other_grid_keys = [k for k in grids if k != grid_key]
    
    grid_o = grid_orientation[0]
    for other_key in other_grid_keys:

        other_grid_orientation_list = grids[other_key]

        for other_grid_o in other_grid_orientation_list:
            is_neighbor, direction = are_neighbors(grid_o, other_grid_o)
            if is_neighbor:
                possible_connections[grid_key].append(other_key)

corner_ids = [k for k in possible_connections if len(possible_connections[k]) == 2]

entry = ([], set(grids.keys()))

def is_goal_fn(node):
    return len(node[1]) == 0

def heuristic_fn(node):
    return len(node[0]) + len(node[1]) * 2

def get_neighbors_fn(node):
    neighbors = []

    # find starting nodes (i.e., add a top left corner)
    if len(node[1]) == num_tiles:
        top_left = corner_ids[0]
        keys_without = set(grids.keys()) - set([top_left])

        for ori_ind, ori in enumerate(grids[top_left]):
            n_node = ([(top_left, ori_ind)], keys_without)
            neighbors.append(n_node)
    
    # for non-starting nodes
    else: 
        # find the index of the tile we're about to place. node[0] is our current flat array of tiles.
        next_tile_ind = len(node[0])

        # is this tile a left edge tile
        is_left = next_tile_ind % width == 0
        tile_to_check = next_tile_ind - width if is_left else next_tile_ind - 1

        # Get tile information from the A* node
        last_tile = node[0][tile_to_check]
        last_tile_key = last_tile[0] 
        last_tile_ori_ind = last_tile[1]
        last_tile_grid = grids[last_tile_key][last_tile_ori_ind]
        
        # Iterate across all possible next tiles for the position to the right (or up, if we're on a left tile)
        for possible_next_tile in possible_connections[last_tile_key]:

            # Enumerate through all possible orientations of possible next tile
            for ori_ind, ori in enumerate(grids[possible_next_tile]):

                # if our last tile and the current orientation of this tile we're looking at are neighbors, 
                is_neighbor, direction = are_neighbors(last_tile_grid, ori)
                if is_neighbor and ((is_left and direction == 3) or (not is_left and direction == 0)):
                    tile_array = node[0][:]
                    new_tile = (possible_next_tile, ori_ind)
                    tile_array.append(new_tile)
                    remaining_tiles = node[1] - set([possible_next_tile])
                    new_node = (tile_array, remaining_tiles)
                    neighbors.append(new_node)
                    break

    return neighbors
    
grid_layout_flat = astar(
    start = entry,
    is_goal_fn = is_goal_fn,
    heuristic_fn = heuristic_fn,
    cost_fn = lambda a, b: 1,
    get_neighbors_fn = get_neighbors_fn,
    get_key_fn = lambda n: str(n),
    include_final_node = True
)[1][0]

final = array([])

gridz = [grids[i[0]][i[1]] for i in grid_layout_flat]

for y in range(width):
    row = array([])
    for x in range(width):
        grid_no, ori = grid_layout_flat[x + (width * y)]
        cell = grids[grid_no][ori]

        cell = cell[1:-1]
        for zi in range(len(cell)):
            cell[zi] = cell[zi][1:-1]
        
        cell = array(cell)
        if len(row) == 0:
            row = cell
        else:
            row = concatenate((row, cell), axis=1)

    if len(final) == 0:
        final = row
    else:
        final = concatenate((final, row))
final = final.tolist()

final_orientations = get_grid_orientations(final)

sea_monster = [
    [18],
    [0, 5, 6, 11, 12, 17, 18, 19],
    [1, 4, 7, 10, 13, 16]
]

def is_sea_monster(grid, x, y):
    ''' we love impure functions here! '''
    has_sea_monsters = True
    for sm_y in range(len(sea_monster)):
        for sm_x in sea_monster[sm_y]:
            if grid[y + sm_y][x + sm_x] == '.': 
                return False

    if has_sea_monsters:
        for sm_y in range(len(sea_monster)):
            for sm_x in sea_monster[sm_y]:
                grid[y + sm_y][x + sm_x] = 'O'

    return has_sea_monsters

def get_roughness(orientations):
    for final_orientation in final_orientations:
        sea_monsters = 0

        for y in range(len(final_orientation) - 1):
            for x in range(len(final_orientation) - 19):
                if is_sea_monster(final_orientation, x, y):
                    sea_monsters += 1
            
        if sea_monsters > 0:
            return sum(1 for y in final_orientation for x in y if x == '#')

print(get_roughness(final_orientations))