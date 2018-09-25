#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Huffman Tree
from BinTree_with_class import BinTNode
from PrioQueue import PrioQueue

class HTNode(BinTNode):
    def __it__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)

def HuffmanTree(weights):
    # weights: literable
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    # trees = HuffmanPrioQ(weights)
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()

# Huffman encoding




