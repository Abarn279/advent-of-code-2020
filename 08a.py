with open('./inp/08.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

seen = set()
acc = 0
i = 0
while i < len(inp):
    if i in seen: break

    op, val = inp[i].split(' ')
    val = int(val)

    if op == 'acc': acc += val
    elif op == 'jmp': i += val;continue

    seen.add(i)
    i += 1

print(acc)