with open('./inp/08.txt') as f:
    orig = [line.rstrip() for line in f.readlines()]

for inst_change in range(len(orig)):
    inp = orig[:]

    if inp[inst_change][:3] == 'jmp':
        inp[inst_change] = 'nop' + inp[inst_change][3:]
    elif inp[inst_change][:3] == 'nop':
        inp[inst_change] = 'jmp' + inp[inst_change][3:]
    else:
        continue

    found = True
    seen = set()
    acc = 0
    i = 0
    while i < len(inp):
        if i in seen: found=False;break

        op, val = inp[i].split(' ')
        val = int(val)

        if op == 'acc': acc += val
        elif op == 'jmp': seen.add(i);i += val;continue

        seen.add(i)
        i += 1

    if found: break

print(acc)