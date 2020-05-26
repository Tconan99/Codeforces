# https://codeforces.com/contest/1358/problem/A

import sys
import os
import heapq
import math

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
    arr = list(map(int, input().split(" ")))
    x1, y1, x2, y2 = arr[0], arr[1], arr[2], arr[3]
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    if x < y:
        x, y = y, x
    
    print(x * y + 1)