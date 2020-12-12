from aoc_utils import Vector2

with open('./inp/12.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

f_directions = {0:Vector2(1, 0),1:Vector2(0, 1),2:Vector2(-1, 0),3:Vector2(0,-1)}
f_delta = {'R':-1,'L':1}
c_directions = {"E":Vector2(1, 0),"N":Vector2(0, 1),"W":Vector2(-1, 0),"S":Vector2(0,-1)}
f_cmds = set(['R','L','F'])
c_cmds = set(['E','N','W','S'])

d = 0
pos = Vector2(0, 0)
for i in inp:
    cmd, amt = i[0], int(i[1:])
    if cmd in f_cmds:
        if cmd == 'F':
            pos += (f_directions[d] * amt)
        else:
            d = (d + (f_delta[cmd] * (amt // 90))) % 4
    elif cmd in c_cmds:
        pos += c_directions[cmd] * amt
print(pos.manhattan_distance(Vector2(0, 0)))
