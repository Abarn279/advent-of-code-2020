import re 

# Class representing a program
class Prog:
    def __init__(self, mask: str):
        self.mask = mask
        self.commands = []

# Get input
with open('./inp/14.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

# Lambda to set a bit at a specific number
set_bit = lambda num, bit_no, new_bit: num | (1 << bit_no) if new_bit == 1 else num & ~(1 << bit_no)

# Parse input into separate programs
progs = []
prog = None
for line in inp:
    if line.startswith('mask'):
        if prog is not None: progs.append(prog)
        prog = Prog(line.split(' = ')[1])
    else:
        key, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
        prog.commands.append(tuple(map(int, (key, val))))
progs.append(prog)

# Run programs
addresses = {}
for prog in progs:
    mask = prog.mask[::-1]

    for command in prog.commands:
        val = command[1]
        for i in range(36):
            if mask[i].isdigit():
                val = set_bit(val, i, int(mask[i]))
        addresses[command[0]] = val

print(sum(i for i in addresses.values()))