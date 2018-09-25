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

def Tree(data, *subtrees):
    tree = [data]
    tree.extend(subtrees)
    return tree

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i + 1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i + 1] = subtree

if __name__ == '__main__':
    t1 = Tree('+', 1, 2, 3)
    t2 = Tree('*', t1, 6, 8)
    set_subtree(t1, 2, Tree('+', 3, 5))
    print(t1)
    