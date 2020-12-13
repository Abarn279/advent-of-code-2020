from aoc_utils import Vector2

with open('./inp/12.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

def rotate_point(p, d):
    if d > 0: d -= 360
    if d == -90: return Vector2(-p.y, p.x)
    if d == -180: return Vector2(-p.x, -p.y)
    if d == -270: return Vector2(p.y, -p.x)

facing_commands = set(['R','L','F'])
cardinal_directions = {"E":Vector2(1, 0),"N":Vector2(0, 1),"W":Vector2(-1, 0),"S":Vector2(0,-1)}
cardinal_cmds = set(['E','N','W','S'])

ship = Vector2(0, 0)
waypoint = Vector2(10, 1)

for i in inp:
    cmd, amt = i[0], int(i[1:])
    if cmd in facing_commands:
        if cmd == 'F':
            ship += waypoint * amt
        else:
            waypoint = rotate_point(waypoint, amt if cmd == 'R' else -amt)
    elif cmd in cardinal_cmds:
        waypoint += cardinal_directions[cmd] * amt
print(ship.manhattan_distance(Vector2(0, 0)))
