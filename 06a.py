# less golfed
with open('./inp/06.txt') as f:
    inp = list(map(lambda s: s.replace('\n', ''), f.read().split('\n\n')))

print(sum(len(set(list(i))) for i in inp))

# golfed
print(sum(len(set(list(i))) for i in list(map(lambda s: s.replace('\n', ''), open('./inp/06.txt').read().split('\n\n')))))