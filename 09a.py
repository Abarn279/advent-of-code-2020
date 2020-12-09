import itertools

with open('./inp/09.txt') as f:
    inp = list(map(int, [line.rstrip() for line in f.readlines()]))

''' 
###
# PART A 
### 
'''
prev = 25

for curr in range(prev, len(inp)):
    check = inp[curr]
    combos = list(itertools.combinations(inp[curr-prev:curr], 2))
    if not any(i + j == check for i, j in combos): break

answer = check
print(answer)

''' 
###
# PART B
### 
'''
def get_rnge():
    global inp
    global answer
    
    answer_pos = inp.index(answer)
    inp = inp[:answer_pos]

    for c_size in range(2, len(inp)):
        for start in range(0, len(inp) - c_size - 1):
            rnge = inp[start:start+c_size]
            if sum(rnge) == answer:
                return rnge

rnge = list(sorted(get_rnge()))
print(rnge[0] + rnge[-1])