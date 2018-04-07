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
from SStack import SStack

class BinTNode:
    def __init__(self, dat, left, right):
        self.data = dat
        self.left = left
        self.right = right

class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def preorder_elements(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()
