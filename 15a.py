from collections import defaultdict

# Get input
inp = '2,0,1,7,4,14,18'
turns = 30000000

# Set up dictionary
starting_no = list(map(int, inp.split(',')))
times_dict = defaultdict(lambda: [])
times_dict.update([(i[1], [i[0] + 1]) for i in enumerate(starting_no)])
last = starting_no[-1]

# Run turns
for turn in range(len(starting_no) + 1, turns + 1):
    if len(times_dict[last]) > 1:
        last = times_dict[last][-1] - times_dict[last][-2] 
    else:
        last = 0
    times_dict[last].append(turn)

print(last)