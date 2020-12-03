import re

with open('./inp/02.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

valid = 0
for line in inp:
    [one, two, char, pw] = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    positions = pw[int(one) - 1] + pw[int(two) - 1]
    if char in positions and positions[0] != positions[1]:
        valid += 1
    
print(valid)
