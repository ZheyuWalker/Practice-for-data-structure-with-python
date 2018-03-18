#!/usr/bin/env python
#-*- coding:utf-8 -*-

from LinkedList import LNode, LList1
# Double-Linked List
class DLNode(LNode):
    def __init__(self, elem, prev = None, next_ = None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head: 
            p.next.prev = p
        else: # 空表
            self._rear = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head:
            p.prev.next = p
        else: # 空表
            self.head = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head.elem
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear:
            self._rear.next = None
        else:
            self._head = None
        return e
random.seed(1)
mList1 = LList1()
mList1.prepend(98)
for i in range(11, 20):
    mList1.append(random.randint(1,20))
for x in mList1.filter(lambda y: y%2 == 0):
    print(x)
