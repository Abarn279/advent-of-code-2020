import sys
sys.setrecursionlimit(50000)

rules_memo = { }

def get_possible_strings_for_rule(rule):
    if rule in rules_memo:
        return rules_memo[rule]

    possible = None
    if rule.startswith('\"'):
        possible = set(rule[1:-1])
    elif '|' in rule:
        a, b = rule.split(' | ')
        possible = get_possible_strings_for_rule(a).union(get_possible_strings_for_rule(b))
    else:
        if len(rule.split(' ')) == 1:
            possible = get_possible_strings_for_rule(rules[int(rule)])
        elif len(rule.split(' ')) == 2:
            a, b = list(map(int,rule.split(' ')))
            poss_a, poss_b = get_possible_strings_for_rule(rules[a]), get_possible_strings_for_rule(rules[b])
            possible = set((i + j for i in poss_a for j in poss_b))
        else:
            a, b, c = list(map(int,rule.split(' ')))
            poss_a, poss_b, poss_c = get_possible_strings_for_rule(rules[a]), get_possible_strings_for_rule(rules[b]), get_possible_strings_for_rule(rules[c])
            possible = set((i + j + k for i in poss_a for j in poss_b for k in poss_c))
    
    rules_memo[rule] = possible
    return possible

# get input
with open('./inp/19.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i.split(': ')[0]):i.split(': ')[1] for i in rules.split('\n')}
    messages = messages.split('\n')

# part 2
rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

s = get_possible_strings_for_rule(rules[0])
print(sum(1 for i in messages if i in s))