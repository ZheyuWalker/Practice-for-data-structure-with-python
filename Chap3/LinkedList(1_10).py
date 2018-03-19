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
    # Insert sort
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                '''
                temp = p.elem
                p.elem = x
                x = temp
                '''
                p.elem, x = x, p.elem
                p = p.next
            crt.elem = x
            crt = crt.next

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem:
            p = self._head
            q = None
            while p and p.elem <= rem.elem:
                q = p
                p = p.next
            if q:
                q.next = rem
            else:   # 表头插入
                self._head = rem
            q = rem
            rem = rem.next
            q.next = p

    # practice1 - del_first, del_last
    def del_first(self):
        if self._head is None:
            raise LinkedListUnderflow
        self._head = self._head.next

    def del_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        elif self._head.next is None:
            self._head = None
        else:
            p = self._head
            while p.next.next:
                p = p.next
            p.next = None
    
    # practice2 - del_(i), insert(i)
    def del_(self, i):
        if i >= len(self):
            raise LinkedListUnderflow
        if i == 0:
            self.del_first()
        p = self._head
        for k in range(i-1):
            p = p.next
        p.next = p.next.next

    def insert(self, i, elem):
        if i > len(self):
            raise LinkedListUnderflow
        if i == 0:
            self.prepend(elem)
        else:
            p = self._head
            for k in range(i-1):
                p = p.next
            p.next = LNode(elem, p.next)

    # practice3 - __len__
    def __len__(self):
        p = self._head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    # practice4 - __eq__, __lt__, __gt__
    def __eq__(self, another):
        if len(self) != len(another):
            return False
        p, q = self._head, another._head
        while p and q:
            if p.elem != q.elem:
                return False
            p, q = p.next, q.next
        return True

    def __lt__(self, another):
        p, q = self._head, another._head
        if p is None and q is None:
            return False
        while p and q:
            if p. elem == q.elem:
                p, q = p.next, q.next
            elif p.elem > q.elem:
                return False
            else:
                return True
        if p is None:
            return True
        else:
            return False  

    def __gt__(self, another):
        if self == another or self < another:
            return False
        else:
            return True

    # practice5 - LinkedList->list & list->LinkedList
    def from_list(self, list_=[]):
        if list_:
            self._head = LNode(list_[0])
        else: 
            self._head = None
        p = self._head
        for i in list_[1:]:
            p.next = LNode(i, p.next)
            p = p.next

    def to_list(self, delete = False):
        if self.is_empty():
            return []
        p = self._head
        list_ = []
        while p:
            list_.append(p.elem)
            p = p.next
        if delete:
            self._head = None
        return list_

    # practice6 - rev_visit(self, operation)
    def rev(self):
        p = None
        while self._head:
            temp = self._head
            self._head = temp.next
            temp.next = p
            p = temp
        self._head = p

    def rev_visit(self, op):
        self.rev()
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        while p:
            op(p.elem)
            p = p.next
        self.rev()

    # practice7 - del_minimal, del_if, drop_duplicate
    def del_minimal(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head.next
        min_val = self._head.elem
        while p:
            if p.elem < min_val:
                min_val = p.elem
            p = p.next
        p = self._head
        while p.next:
            if p.next.elem == min_val:
                p.next = p.next.next
            p = p.next
        if self._head.elem == min_val:
            self._head = self._head.next

    def del_if(self, pred):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        while p.next:
            if pred(p.next.elem):
                p.next = p.next.next
            else:
                p = p.next
        if pred(self._head.elem):
            self._head = self._head.next

    def del_duplicate(self):
        if self._head is None:
            raise LinkedListUnderflow
        elements = [self._head.elem]
        p = self._head
        while p.next:
            if p.next.elem in elements:
                p.next = p.next.next
            else:
                elements.append(p.next.elem)
                p = p.next

    # practice8 - interleaving
    def interleaving(self, another):
        p, q = self._head, another._head
        if p is None or q is None:
            self._head = another._head if q else self._head 
            return
        while p.next and q:
            m, n = p.next, q.next
            q.next = p.next
            p.next = q
            p, q = m, n
        if p.next is None:
            p.next = q

    # practice9 - sort0(未能完全理解题意)
    def sort0(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head.next
        self._head.next = None
        while p:
            q = self._head
            if p.elem <= self._head.elem:
                self._head = p
                p = p.next
                self._head.next = q
                continue
            while q and q.next:
                if q.next.elem < p.elem:
                    q = q.next
                else: 
                    break
            temp = q.next
            q.next = p
            p = p.next
            q.next.next = temp

    # practice10 - partition 
    def partition(self, pred):
        if self._head is None:
            raise LinkedListUnderflow
        another = LList()
        p = self._head
        count = 0
        while p.next:
            if pred(p.next.elem):
                another.append(p.next.elem)
                p.next = p.next.next
            else:
                p = p.next
        if pred(self._head.elem):
            another.prepend(self._head.elem)
            self._head = self._head.next
        return another, self


mList1 = LList()
mList2 = LList()
for i in range(10):
    mList1.prepend(i)
    mList2.prepend(i)
for i in range(1, 10):
    mList1.append(i)
    mList2.append(i)
mList1.printall()
print('mList1 == mList2 is', mList1 == mList2)
'''
mList1.for_each(print)
for x in mList1.elements():
    print(x)
'''
mList1.sort()
mList1.printall()
print('mList1 < mList2 is', mList1 < mList2)
mList1.del_(2)
mList1.printall()
mList1.insert(0, 10)
mList1.printall()
print('mList1 > mList2 is', mList1 > mList2)
print(len(mList1))
# practice5
mList1.from_list([1, 2, 's'])
mList1.printall()
print(mList1.to_list())
# practice6
mList1.rev_visit(print)
# practice7
mList2.sort()
mList2.del_minimal()
mList2.printall()
mList2.del_if(lambda x: x<=6)
mList2.printall()
mList2.del_duplicate()
mList2.printall()
#practice8
mList3 = LList()
mList3.from_list([27, -1])
mList2.interleaving(mList3)
mList2.printall()
#practice9
mList2.sort0()
mList2.printall()
#practice10
x, y = mList2.partition(lambda x: x%3 == 0)
x.printall()
y.printall()



# 带尾指针的链表结构
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
'''
random.seed(3)
mList1 = LList1()
mList1.prepend(98)
for i in range(11, 20):
    mList1.append(random.randint(1,20))
for x in mList1.filter(lambda y: y%2 == 0):
    print(x)
'''
