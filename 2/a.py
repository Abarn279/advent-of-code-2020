import re

with open('./2.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

valid = 0
for line in inp:
    [low, high, char, pw] = re.match('(\d+)-(\d+) (\w): (\w+)', line).groups()
    
    count = len([i for i in pw if i == char])

    if count >= int(low) and count <= int(high): valid += 1

print(valid)
