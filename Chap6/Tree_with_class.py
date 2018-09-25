#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
ADT Tree:
    Tree(self, data, forest)
    is_empty(self)
    num_nodes(self)
    data(self)
    first_child(self, node)
    children(self, node)
    set_first(self, tree)
    insert_child(self, i, tree)
    traversal(self)
    forall(self, op)
'''

class SubtreeIndexError(ValueError):
    pass

class TreeNode:
    def __init__(self, data, subs={}):
        self._data = data
        self._subtrees = list(subs)

    def __str__(self):
        return '[TreeNode {0} {1}]'.format(self._data,
                                            self._subtrees)

class Tree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

