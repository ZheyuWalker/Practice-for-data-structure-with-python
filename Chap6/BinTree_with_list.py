#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
ADT BinTree:
    BinTree(self, data, left, right)    # create a new binary tree
    is_empty(self)                      
    num_nodes(self)
    data(self)
    left(self)              # get its left subtree
    right(self)
    set_left(self, btree)   # replace origin left subtree with btree    
    set_right(self, btree)
    traversal(self)         # traverse all nodes
    forall(self, op)        # excute operation 'op' for all nodes
'''
# BinTree with list
def BinTree(data, left = None, right = None):
    return [data, left, right]

def is_empty_BTree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_left(btree, left):
    btree[1] = left

def set_right(btree, right):
    btree[2] = right

# make expression in BinTree with tuple 
def make_sum(a, b):
    return ('+', a, b)

def make_prod(a, b):
    return ('*', a, b)

def make_diff(a, b):
    return ('-', a, b)

def make_div(a, b):
    return ('/', a, b)

def is_basic_exp(e):
    return not isinstance(e, tuple)

def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or 
            isinstance(x, complex))

# evaluate defined expression
def eval_exp(e):

    def eval_sum(a, b):
        if is_number(a) and is_number(b):
            return a + b
        if is_number(a) and a == 0:
            return b
        if is_number(b) and b == 0:
            return a
        return make_sum(a, b)

    def eval_div(a, b):
        if is_number(a) and is_number(b):
            return a / b
        if is_number(a) and a == 0:
            return 0
        if is_number(b) and b == 1:
            return a
        if is_number(b) and b == 0:
            raise ZeroDivisionError
        return make_div(a, b)

    def eval_prod(a, b):
        if is_number(a) and is_number(b):
            return a * b
        return make_prod(a, b)

    def eval_diff(a, b):
        if is_number(a) and is_number(b):
            return a - b
        return make_diff(a, b)
    # judge is e is an operator
    if is_basic_exp(e):
        return e
    # Recurrsion
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError('Unknown operator:', op)

    


if __name__ == '__main__':
    e1 = make_prod(3, make_sum(2,5))
    e2 = make_sum(make_prod(-1, 2), make_prod(3, 7))
    print(e1)
    print(e2)
    print(eval_exp(e1))
    print(eval_exp(e2))