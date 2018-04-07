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

class SStack():         # Stack based on sequence table(list)
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.pop()')
        return self._elems.pop()

if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
    # reverse
    st1 = SStack()
    for x in list(range(1,20,2)):
        st1.push(i)
    list_ = []
    while not st1.is_empty():
        list_.append(st1.pop())