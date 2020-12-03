import re

with open('./inp/02.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

valid = 0
for line in inp:
    [low, high, char, pw] = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    
    count = len([i for i in pw if i == char])

    if count >= int(low) and count <= int(high): valid += 1

print(valid)
