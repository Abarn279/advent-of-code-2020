import math

def get(s, lowchar, highcar):
    i = 0 # left cursor
    j = 2 ** len(s) - 1 # right cursor
    c = 0  # current character index
    while j - i > 1:
        halfdif = math.ceil((j - i) / 2)

        if s[c] == lowchar:
            j -= halfdif
        elif s[c] == highcar:
            i += halfdif
        c += 1
    return i if s[c] == lowchar else j

getid = lambda s: get(s[:7], 'F', 'B') * 8 + get(s[7:], 'L', 'R')

# get initial input
with open('./inp/05.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

ids = set(getid(i) for i in inp)
[my_seat] = [i for i in range(min(ids), len(ids)) if i not in ids]
print(my_seat)