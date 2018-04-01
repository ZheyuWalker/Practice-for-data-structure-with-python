#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
infix expressions -> prefix expressions
infix expressions -> suffix expressions
infix: (3 - 5) * (6 + 17 * 4) / 3
prefix: / * - 3 5 + 6 * 17 4 3
suffix: 3 5 - 6 17 4 * + * 3 /

Pesudocode for suffix calculation
while expression:
    x = nextItem()
    if x is operand:
        st.push(float(x))   # push x in to stack
    else:                   # x is an operator 
        a = st.pop()        # return the last 2 operands
        b = st.pop()
        ...                 # do calculate
'''
from SStack import SStack
def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()
    # here the program doesn't deal with space and other char 
    for x in exp:
        if x not in operators:
            st.push(float(x))   # x have to be numbers
            continue
        if st.depth() < 2:
            raise SyntaxError('Short of operand(s).')
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a           # May cause ZeroDivisionError
        else:
            break

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError('Extra operand(s).')

# User calling function
def suffix_exp_calculator():
    while True:
        try:
            line = input('Suffix Expression:')
            if line == 'end': return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print('Error:', type(ex), ex.args)