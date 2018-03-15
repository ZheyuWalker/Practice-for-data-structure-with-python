#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
ADT List:                   #抽象数据类型‘表’
    List(self)              #创建一个新表
    is_empty(self)          #判断是否为空
    len(self)               #获取表长
    prepend(self, elem)     #在表前段插入一个新元素
    append(self, elem)      #
    insert(self, elem, i)   #
    del_first(self)
    del_last(self)
    del(self, i)
    search(self, elem)      #查找elem在表中的位置
    forall(self, op)        #对全部元素执行操作op
'''
import random
class LNode:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_
'''
head = LNode(1)
p = head
for i in range(2,11):
    p.next = LNode(i)
    p = p.next

p = head
while p:
    print(p.elem)
    p = p.next
'''
class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self, elem):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next == None:
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end='')
            if p.next:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, proc):
        p = self._head
        while p:
            proc(p.elem)
            p= p.next

    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next
'''
mList1 = LList()
for i in range(10):
    mList1.prepend(i)
for i in range(1, 10):
    mList1.append(i)
mList1.printall()
# mList1.for_each(print)
for x in mList1.elements():
    print(x) 
'''

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        '''
        self._head = LNode(elem, self._head)
        if self._rear is None:
            self._rear = self._head
        '''
        if self._head:
            self._head = LNode(elem, self._head)
        else:
            self._head = LNode(elem, self._head)
            self._rear = self._head

    def append(self, elem):
        if self._head:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
        else:
            self._head = LNode(elem. self._head)
            self._rear = self._head

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

random.seed(3)
mList1 = LList1()
mList1.prepend(98)
for i in range(11, 20):
    mList1.append(random.randint(1,20))
for x in mList1.filter(lambda y: y%2 == 0):
    print(x)
