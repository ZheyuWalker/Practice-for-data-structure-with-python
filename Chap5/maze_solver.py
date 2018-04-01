#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
State Space Search Problem
A set of all possible states
There must be one initial state s0, one or more end state(s)
For each s, it may have 0 or more neighbors -> neighbor(s)
For each s, we can judge if it is valid -> valid(s)
Problem:
    from s0. search or solution to end state(s)
'''
import copy
from SStack import SStack
from SQueue import SQueue

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2
def passable(maze, pos):        # valid(s)
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=' ')
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1]+dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=' ')
                return True
    return False


def maze_solver_stack(maze, start, end):    # depth first search
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if nextp == end:
                print(end, end=' ')
                print(pos, end=' ')
                # print('Succeed!')
                while not st.is_empty():
                    print(st.pop()[0], end=' ')
                print('')
                return 
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print('No path found.')

def maze_solver_queue(maze, start, end):    # width-first search
    if start == end:
        print('Path finds.')
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print('Path finds.')
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)
    print('No path.')

if __name__ == '__main__':
    maze1 =[[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    maze2 = copy.deepcopy(maze1)
    start = (1, 1)
    end = (5, 3)
    # find_path(maze, start, end)
    maze_solver_stack(maze1, start, end)
    maze_solver_queue(maze2, start, end)