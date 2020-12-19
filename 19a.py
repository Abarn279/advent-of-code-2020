def get_possible_strings_for_rule(rule):
    if rule.startswith('\"'):
        return set(rule[1:-1])
    elif '|' in rule:
        a, b = rule.split(' | ')
        return get_possible_strings_for_rule(a).union(get_possible_strings_for_rule(b))
    else:
        if len(rule.split(' ')) == 1:
            return get_possible_strings_for_rule(rules[int(rule)])
        elif len(rule.split(' ')) == 2:
            a, b = list(map(int,rule.split(' ')))
            poss_a, poss_b = get_possible_strings_for_rule(rules[a]), get_possible_strings_for_rule(rules[b])
            return set((i + j for i in poss_a for j in poss_b))
        else:
            a, b, c = list(map(int,rule.split(' ')))
            poss_a, poss_b, poss_c = get_possible_strings_for_rule(rules[a]), get_possible_strings_for_rule(rules[b]), get_possible_strings_for_rule(rules[c])
            return set((i + j + k for i in poss_a for j in poss_b for k in poss_c))

# get input
with open('./inp/19.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i.split(': ')[0]):i.split(': ')[1] for i in rules.split('\n')}
    messages = messages.split('\n')

s = get_possible_strings_for_rule(rules[0])
print(sum(1 for i in messages if i in s))