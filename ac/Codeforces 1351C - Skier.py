# https://codeforces.com/problemset/problem/1351/C

import sys
import os
import heapq

try:
    path = "./file/input.txt"
    if os.path.exists(path):
        sys.stdin = open(path, 'r')
    # sys.stdout = open(r"./file/output.txt", 'w')
except:
    pass

t = int(input())

def printd(value):
    # print(value)
    pass

for _ in range(t):
    path = input()
    currentx = 100000
    currenty = 100000

    map = {}

    result = 0
    for c in path:
        pospre = currentx * 1000000 + currenty

        dir = 0
        if c == 'N':
            currenty += 1
            dir = 1
        if c == 'S':
            currenty -= 1
            dir = 3
        if c == 'W':
            currentx -= 1
            dir = 4
        if c == 'E':
            currentx += 1
            dir = 0

        pospre = pospre * 10 + (4 - dir)

        pos = currentx * 1000000 + currenty
        pos = pos * 10 + dir
        if pos in map:
            result += 1
        else:
            map[pos] = True
            result += 5

        map[pospre] = True
    print(result)
