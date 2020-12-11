from aoc_utils import Grid2d, Vector2

DIRECTIONS = [Vector2.create(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0]

def get_nearest_seat(grid, pos, d):
    pos = pos + d
    while True:
        if pos not in grid:
            return None
        if grid[pos] != '.':
            return grid[pos]
        pos = pos + d

def get_num_surrounding(grid, pos, char): 
    sm = 0
    for d in DIRECTIONS:
        seat = get_nearest_seat(grid, pos, d)
        if seat == char: sm += 1
    return sm

def get_new(grid: Grid2d):
    copy = grid.copy()

    min_b, max_b = grid.get_bounds()

    for y in range(min_b.y, max_b.y + 1):
        for x in range(min_b.x, max_b.x + 1):
            pos = Vector2.create(x, y)
            if grid[pos] == 'L' and get_num_surrounding(grid, pos, '#') == 0:
                copy[pos] = '#'
            elif grid[pos] == '#' and get_num_surrounding(grid, pos, '#') >= 5:
                copy[pos] = 'L'

    return copy

with open('./inp/11.txt') as f:
    grid = Grid2d('.', [line.rstrip() for line in f.readlines()])

last = None
while True:
    new = get_new(grid)
    new_str = str(new)
    if new_str == last:
        break
    last = new_str
    grid = new

print(sum(1 for i in new.values() if i == '#'))
