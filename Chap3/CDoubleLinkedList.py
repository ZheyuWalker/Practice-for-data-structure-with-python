#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
ADT CDLList:                #抽象数据类型‘表’
    CDLList(self)           #创建一个新表
    is_empty(self)          #判断是否为空
    len(self)               #获取表长
    prepend(self, elem)     #在表前段插入一个新元素
    append(self, elem)      #
    pop(self, elem)
    pop_last(self, elem)
    insert(self, elem, i)   #
    del_first(self)
    del_last(self)
    del(self, i)
    search(self, elem)      #查找elem在表中的位置
    forall(self, op)        #对全部元素执行操作op
'''

from DoubleLinkedList import DLNode
from LinkedList_1_10 import LinkedListUnderflow

class CDLList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def __len__(self):
        if self._head is None:
            return 0
        p = self._head.next
        cnt = 1
        while p != self._head:
            cnt += 1
            p = p.next
        return cnt

    def append(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head:
            p.prev = self._head.prev
            p.prev.next = p
            self._head.prev = p
        else:
            self._head = p
            self._head.prev = self._head
            self._head.next = self._head

    def prepend(self, elem):
        self.append(elem)
        self._head = self._head.prev

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head.prev
        e = self._head.elem
        if p == self._head:
            self._head = None
        else:
            p.next = p.next.next
            self._head.next.prev = p
            self._head = p.next
        return e

    def pop_last(self):
        if self._head is None:
            raise  LinkedListUnderflow
        p = self._head.prev
        e = self._head.prev.elem
        if p == self._head:
            self._head = None
        else:
            self._head.prev = p.prev
            p.prev.next = self._head
        return e
            
    def printall(self):
        p = self._head
        while p:
            print(p.elem, end='')
            if p.next != self._head:
                print(', ', end='')
                p = p.next
            else:
                break
        print('')

if __name__ == '__main__':
    mList1 = CDLList()
    # prepend & append
    for i in range(10):
        mList1.prepend(i)
    for i in range(11, 20):
        mList1.append(i)
    mList1.printall()
    # pop and pop_last
    print(mList1.pop())        # this should be 9
    print(mList1.pop_last())   # this should be 19
    mList1.printall()


