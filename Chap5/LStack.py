#！/usr/bin/env python
#-*- coding:utf-8 -*-

'''
ADT Stack:
    Stack(self)         #create an empty stack
    is_empty(self)      
    push(self, elem)
    pop(self)
    top(self)
'''

class StackUnderflow(ValueError):
    pass

class LNode(object):
    def __init__(self, elem, next_):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):         # Create an empty stack
         self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow('in LStack.top()')
        return self._top.elem

    def push(self, elem):
        p = LNode(elem, self._top)
        self._top = p

    def pop(self):
        if self._top is None:
            raise StackUnderflow('in LStack.pop()')
        p = self._top
        self._top = self._top.next
        return p.elem