#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Practice8 -- Ackerman Function
            n+1                     if m == 0
Ack(m, n) = Ack(m-1, 1)             if m != 0 and n == o
            Ack(m-1, Ack(m, n-1))   if m != 0 and n != 0
'''

from SStack import SStack

# Recursive
def Ack_r(m, n):
    # print('m = {}, n = {}'.format(m, n))
    if m == 0:
        return n+1
    elif n == 0:
        return Ack_r(m-1, 1)
    else:
        t = Ack_r(m, n-1)
        return Ack_r(m-1, t)

# Loop
def Ack_l(m, n):
    st = SStack()
    st.push(m)
    while not st.is_empty():
        m = st.pop()
        if m == 0:
            n += 1
        elif n == 0:
            st.push(m-1)
            n = 1
        elif n != 0:
            st.push(m-1)
            st.push(m)
            n -= 1
    return n

if __name__ == '__main__':
    print(Ack_r(3, 4))
    print(Ack_l(3, 4))