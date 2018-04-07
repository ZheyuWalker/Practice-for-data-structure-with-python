#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
ADT Queue:
    Queue(self)             # create an empty queue
    is_empty(self)      
    enqueue(self, elem)     # add a new elem to the queue
    dequeue(self)           # delete the first added elem
    peek(self)              # access the first added elem
'''

class QueueUnderflow(ValueError):
    pass

class SQueue:
    def __init__(self, init_len = 8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow('in peek for SQueue')
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow('in dequeue for SQueue')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+1) % old_len]
        self._elems, self._head = new_elems, 0