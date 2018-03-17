class LNode(object):
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class  LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 前端弹出
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CLList')
        p = self._rear.next
        # 判断表长度是否为1
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
mList1 = LCList()
for i in range(10):
    mList1.prepend(i)
for i in range(1, 10):
    mList1.append(i)
mList1.printall()
# mList1.for_each(print)
for x in mList1.elements():
    print(x) 
