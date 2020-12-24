def get_splits(st):
    for i in range(1, len(st)):
        yield (st[:i], st[i:])

memo = {}
def matches(message, rule):
    if (message, rule) in memo:
        return memo[(message, rule)]

    does_match = False
    # base case. single char match
    if rule.startswith('\"'):
        does_match = message == rule[1:-1]

    # 'or'. call with each side
    elif '|' in rule:
        a, b = rule.split(' | ')
        does_match = matches(message, a) or matches(message, b)

    else:
        # single number
        if len(rule.split(' ')) == 1:
            does_match = matches(message, rules[int(rule)])

        else:
            # multiple nums 'and' together
            sub_rules = rule.split(' ')
            for pre, post in get_splits(message):
                if matches(pre, sub_rules[0]) and matches(post, ' '.join(sub_rules[1:])):
                    does_match = True
                    break
    
    memo[(message, rule)] = does_match
    return does_match

# get input
with open('./inp/19.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i.split(': ')[0]):i.split(': ')[1] for i in rules.split('\n')}
    messages = messages.split('\n')

# uncomment for part 2
rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

print(sum(1 for i in messages if matches(i, rules[0])))