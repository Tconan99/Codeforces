# https://codeforces.com/problemset/problem/1365/C

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

t = 1 # int(input())

def printd(value):
    # print(value)
    pass

def case():
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    mapp = [0] * (n + 1)
    for index, value in enumerate(a):
        mapp[value] = index

    result = 0
    right = [0] * (n + 1)
    for index, value in enumerate(b):
        pos = mapp[value]
        if pos < index:
            pos += n
        right[pos - index] += 1
        result = max(result, right[pos - index])
    
    print(result)
    
for _ in range(t):
    case()