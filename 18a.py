from collections import deque
from operator import add, mul

ops = {'*': mul, '+': add}
op_prio = {'*': 0, '+': 1}

def sort_postfix(expr):
    ''' sort an expression into postfix notation '''
    expr_l = expr.split(' ')

    # part 1 sort algo
    # for i in range(2, len(expr_l), 2): 
    #     expr_l[i - 1], expr_l[i] = expr_l[i], expr_l[i - 1]
    # final = expr_l

    # part 2 sort algo - http://www.cs.nthu.edu.tw/~wkhon/ds/ds10/tutorial/tutorial2.pdf
    final = []
    stack = deque()
    for i in expr_l:
        if i.isdigit(): 
            final.append(i)
        else:
            if len(stack) == 0:
                stack.appendleft(i)
            else:
                while len(stack) > 0 and op_prio[stack[0]] >= op_prio[i]:
                    final.append(stack.popleft())
                stack.appendleft(i)
    for i in stack:
        final.append(i)
    
    return ' '.join(final)

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

    # sort into postfix notation queue, create stack, evaluate
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