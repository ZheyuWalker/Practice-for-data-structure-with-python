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

class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left =left
        self.right = right

def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) \
                 + count_BinTNodes(t.right)

def sum_BinTnodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTnodes(t.left) \
                      + sum_BinTnodes(t.right)

# Traversal with Recurrsion
def preorder(t, proc):
    # proc is the process for data in all nodes
    assert(isinstance(t, BinTNode))
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)

def inorder(t, proc):
    assert(isinstance(t, BinTNode))
    if t is None:
        return
    inorder(t.left, proc)
    proc(t.data)
    inorder(t.right, proc)

def postorder(t, proc):
    assert(isinstance(t, BinTNode))
    if t is None:
        return
    postorder(t.left, proc)
    postorder(t.right, proc)
    proc(t.data)

def print_BinTNodes(t):
    if t is None:
        print('^', end='')  # Empty Tree
        return
    print('(' + str(t.data) + ' ', end='')
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(')',end='')

# Breadth-first Traversal with Queue
from SQueue import *

def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)

# Depth-first Traversal with Stack
from SStack import SStack

def preorder_s(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

# Generator
def preorder_elems(t):
    s =SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

def inorder_s(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right

# myself postorder traversal algorithm
def postorder_s(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push((t, t.right))
            t = t.left
        (m, n) = s.pop()
        if n:
            s.push((m, None))
            t = n
        else:
            proc(m.data)

def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None

if __name__ == '__main__':
    t1 = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
    t2 = BinTNode(2, None, BinTNode(12, BinTNode(6), BinTNode(7)))
    t = BinTNode(0, t1, t2)
    print_BinTNodes(t), print('')
    f = lambda x: print(x, end=' ')
    preorder_s(t, f), print('')
    inorder_s(t, f), print('')
    postorder_s(t, f), print('')
    postorder_nonrec(t, f), print('')
