#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Practice12 -- Eight Queens Puzzle

'''
#from SStack import SStack
class Board():
    def __init__(self, n):
        self._board = []
        for i in range(n):
            self._board.append(n * [0])

    def place_queen(self, i, j):
        # i: line index
        # j: column index
        n = len(self._board)
        if self._board[i][j] == 0:
            self._board[i] = [x+1 for x in self._board[i]]
            for k in range(n):
                self._board[k][j] += 1
                if k < i:
                    if j-(i-k) >= 0:
                        self._board[k][j-i+k] += 1
                    if j+(i-k) <= n-1:
                        self._board[k][j+i-k] += 1
                elif k > i:
                    if j-(k-i) >= 0:
                        self._board[k][j+i-k] += 1
                    if j+(k-i) <= n-1:
                        self._board[k][j-i+k] += 1
        else:
            return False

    def take_queen(self, i, j):
        if self._board[i][j] != 2:
            raise ValueError
        n = len(self._board)
        self._board[i] = [x-1 for x in self._board[i]]
        for k in range(n):
            self._board[k][j] -= 1
            if k < i:
                if j-(i-k) >= 0:
                    self._board[k][j-i+k] -= 1
                if j+(i-k) <= n-1:
                    self._board[k][j+i-k] -= 1
            elif k > i:
                if j-(k-i) >= 0:
                    self._board[k][j+i-k] -= 1
                if j+(k-i) <= n-1:
                    self._board[k][j-i+k] -= 1
    
    def placeable(self, i, j):
        return self._board[i][j] == 0

    def printall(self):
        for i in self._board:
            print(i)

def eight_queens_solver(b, j = 0):
    # board: a Board object
    # i, j: start place
    i, n = 0, len(b._board)
    st = []
    if b.placeable(i, j):
        b.place_queen(i, j)
        st.append((i,j))
        i += 1
    while len(st) < n:
        while j < n:
            # print('i = {}, j = {}'.format(i, j))
            if b.placeable(i, j):
                finded = True
                b.place_queen(i, j)
                # print('i = {}, j = {}'.format(i, j))
                st.append((i, j))
                i += 1
                break
            else:
                j += 1
        if j == n:
            (i, j) = st.pop()
            b.take_queen(i, j)
            j += 1
            while j < n:
                if b.placeable(i, j):
                    b.place_queen(i, j)
                    st.append((i, j))
                    i += 1
                    j = 0
                    break
                else:
                    j += 1
        # print(st)
    return st


if __name__ == '__main__':
    b = Board(8)
    b.printall()
    '''
    b.printall()
    print('')
    b.place_queen(3, 2)
    b.printall()
    print('')
    b.place_queen(0, 0)
    b.take_queen(3, 2)
    b.printall()
    '''
    print(eight_queens_solver(b))