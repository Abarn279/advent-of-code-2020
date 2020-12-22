from collections import deque
from aoc_utils import id_gen

seen_rounds = set()
id_gen = id_gen(1)

def get_round_rep(p1, p2, game):
    return f"{str(game)}/{','.join(str(i) for i in p1)}/{','.join(str(j) for j in p2)}"

def simulate_combat(p1, p2):
    ''' simulate. return 1 if winner is p1, else 2 '''
    game = next(id_gen) # get id of current game

    while len(p1) > 0 and len(p2) > 0:

        # check if repeat round
        round_rep = get_round_rep(p1, p2, game)
        if round_rep in seen_rounds:
            return 1
        seen_rounds.add(round_rep)

        # draw cards
        c1, c2 = p1.popleft(), p2.popleft()

        # need recursive?
        if len(p1) >= c1 and len(p2) >= c2:
            p1_c, p2_c = deque(list(p1)[:c1]), deque(list(p2)[:c2])
            winner = simulate_combat(p1_c, p2_c)
            if winner == 1: p1.append(c1);p1.append(c2)
            elif winner == 2: p2.append(c2);p2.append(c1)

        # regular non-recursive round
        else:
            if c1 > c2: p1.append(c1);p1.append(c2)
            elif c1 < c2: p2.append(c2);p2.append(c1)

    return 1 if len(p1) > 0 else 2

# Get input
with open('./inp/22.txt') as f:
    p1, p2 = [deque(map(int, i.split('\n')[1:])) for i in f.read().split('\n\n')]

winner = p1 if simulate_combat(p1, p2) == 1 else p2
print(sum([winner.pop() * i for i in range(1, len(winner) + 1)]))