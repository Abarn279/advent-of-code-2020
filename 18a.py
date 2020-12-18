from collections import deque
from operator import add, mul

ops = {'*': mul, '+': add}

def sort_postfix(expr):
    ''' sort an expression into postfix notation '''
    expr_l = expr.split(' ')

    for i in range(2, len(expr_l), 2): 
        expr_l[i - 1], expr_l[i] = expr_l[i], expr_l[i - 1]
    
    return ' '.join(expr_l)

def do_calc(expr):

    # Recursively call for parens
    paren = {}
    for i in range(len(expr)):
        if expr[i] == '(':
            paren['('] = i
        if expr[i] == ')':
            paren[')'] = i
            break
    if len(paren) > 0:
        pre = expr[:paren['(']]
        solved = str(do_calc(expr[paren['(']+1:paren[')']]))
        post = expr[paren[')'] + 1:]
        expr = pre + solved + post
        return do_calc(expr)

    # sort into postfix queue, create stack
    q = deque(sort_postfix(expr).split(' '))
    s = deque()

    while len(q) > 0:
        if q[0].isdigit():
            s.appendleft(q.popleft())
        else:
            op = ops[q.popleft()]
            s.appendleft(op(int(s.popleft()), int(s.popleft())))

    return s[0]
    
# get input
with open('./inp/18.txt') as f:
    inp = [line.rstrip() for line in f.readlines()]

print(sum(do_calc(i) for i in inp))