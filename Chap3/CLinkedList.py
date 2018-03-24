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

    # practice11
    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop_last of CLList')
        p = self._rear
        if p.next == p:
            self._rear = None
            return p.elem
        while p.next != self._rear:
            p = p.next
        self._rear = p
        p.next = p.next.next

    def find(self, pred):
        if self._rear is None:
            raise LinkedListUnderflow('in find of CLList')
        p = self._rear.next
        while p:
            if p == self._rear:
                break
            if pred(p.elem):
                return p.elem
            p = p.next 
        if pred(self._rear.elem):
            return self._rear.elem

    def filter(self, pred):
        if self._rear is None:
            raise LinkedListUnderflow('in filter of CLList')
        p = self._rear.next
        while p:
            if p == self._rear:
                break
            if pred(p.elem):
                yield p.elem
            p = p.next
        if pred(self._rear.elem):
            yield self._rear.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem, end='')
            if p is self._rear:
                print('')
                break
            else:
                print(', ', end='')
            p = p.next


    def sort(self):
        p = self._rear
        if p is None or p.next == p:
            return
        head = self._rear.next
        rem = head.next
        head.next = None
        self._rear.next = None
        while rem:
            p = head
            q = None
            while p and p.elem < rem.elem:
                q = p
                p = p.next
            if q:
                q.next = rem
            else:
                head = rem
            q = rem
            rem = rem.next
            q.next = p
        self._rear = head
        while self._rear.next:
            self._rear  = self._rear.next
        self._rear.next = head

    def __len__(self):
        length = 0
        if self._rear is None:
            return length
        p = self._rear.next
        while p:
            length += 1
            if p is self._rear:
                break
            p = p.next
        return length

    def del_(self, i):
        if i >= len(self):
            raise LinkedListUnderflow
        p = self._rear
        for k in range(i):
            p = p.next
        if p.next == self._rear:
            self._rear = p
        p.next = p.next.next

    def del_if(self, pred):
        if self._rear is None:
            raise LinkedListUnderflow
        p = self._rear.next
        q = self._rear
        while p != self._rear:
            if pred(p.elem):
                p = p.next
                q.next = p
            else:
                q = p
                p = p.next
        if pred(self._rear.elem):
            self._rear = q
            q.next = p.next

    def del_duplicate(self):
        if self._rear is None:
            raise LinkedListUnderflow
        list_ = []
        p = self._rear.next
        q = self._rear
        while p != self._rear:
            if p.elem in list_:
                p = p.next
                q.next = p
            else:
                list_.append(p.elem)
                q = p
                p = p.next
        if self._rear.elem in list_:
            self._rear = q
            q.next = p.next

    def insert(self, i, elem):
        if i > len(self):
            raise LinkedListUnderflow
        p = self._rear
        for k in range(i):
            p = p.next
        if p == self._rear:
            if i == 0:
                self.prepend(elem)
            else:
                self.append(elem)
        else:
            p.next = LNode(elem, p.next)

    def rev(self):
        p = self._rear
        if p is None or p.next is None:
            return
        p = self._rear.next
        self._rear.next = None
        new_rear = p
        temp = None
        while p != self._rear:
            q = p
            p = p.next
            q.next = temp
            temp = q 
        p.next = q
        new_rear.next = p
        self._rear = new_rear

mList1 = LCList()
for i in range(10):
    mList1.prepend(i)
for i in range(1, 10):
    mList1.append(i)
mList1.printall()
# practice11 -- pop_last
mList1.pop_last()
mList1.printall()
# find & filter
print(mList1.find(lambda x: x==5))
for i  in mList1.filter(lambda x: x%3 == 2):
    print(i, end= ', ')
print('')
# sort
mList1.sort()
mList1.printall()
# delete operation
mList1.del_(len(mList1)-1)
mList1.printall()
mList1.del_if(lambda x: x%2==0)
mList1.printall()
mList1.del_duplicate()
mList1.printall()
# insert operation
mList1.insert(0, 'head')
mList1.insert(len(mList1), 'rear')
mList1.printall()
# reverse
mList1.rev()
mList1.printall()