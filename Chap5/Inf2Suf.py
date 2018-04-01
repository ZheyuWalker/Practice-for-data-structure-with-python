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
from suffix_exp_calculator import suf_exp_evaluator
priority = {'(':1, '+':3, '-':3, '*':5, '/':5}
infix_operators = '+-*/()'

def tokens(line): # a generator
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue
        
        j = i + 1
        while (j < llen and not line[j].isspace() and 
               line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E') and 
                 j+1 < llen and line[j+1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j

def Inf2Suf(line):
    st = SStack()
    exp = []

    for x in tokens(line): 
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '('.")
            st.pop()
        else: 
            while (not st.is_empty() and
                     priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())

    return exp

def test_Inf2Suf(s):
    print(s)
    print(trans_infix_suffix(s))
    print('Value:', suf_exp_evaluator(trans_infix_suffix(s)))