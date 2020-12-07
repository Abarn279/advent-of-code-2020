with open('./inp/06.txt') as f:
    inp = f.read().split('\n\n')

same = 0
for g in inp:
    people = g.split('\n')
    if len(people) == 1: 
        same += len(people[0])
        continue
    sets = []
    for p in people:
        s = set(list(p))
        sets.append(s)
    s = sets[0]
    for i in range(1, len(sets)):
        s = s.intersection(sets[i])
    same += len(s)
print(same)