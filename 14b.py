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
    mask = prog.mask[::-1] # Reverse so that mask indeces match up with bit indeces

    for command in prog.commands:
        addresses_to_update = [command[0]]

        for i in range(36): 
            if mask[i] == '0':
                continue
            elif mask[i] == '1':
                for a_i in range(len(addresses_to_update)):
                    addresses_to_update[a_i] = set_bit(addresses_to_update[a_i], i, 1)
            elif mask[i] == 'X':
                new_addresses_to_update = []
                for a in addresses_to_update:
                    new_addresses_to_update.append(set_bit(a, i, 0))
                    new_addresses_to_update.append(set_bit(a, i, 1))
                addresses_to_update = new_addresses_to_update
        
        for a in addresses_to_update:
            addresses[a] = command[1]


print(sum(i for i in addresses.values()))