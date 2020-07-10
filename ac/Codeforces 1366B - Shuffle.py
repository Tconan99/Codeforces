# https://codeforces.com/problemset/problem/1366/B

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

def case():
    arr = list(map(int, input().split(" ")))
    #  𝑛, 𝑥 and 𝑚
    n, x, m = arr[0], arr[1], arr[2]
    ll = x
    rr = x
    for _ in range(m):
        arr = list(map(int, input().split(" ")))
        l, r = arr[0], arr[1]
        if l < ll and r >= ll:
            ll = l
            rr = max(rr, r)
        elif l <= rr and r > rr:
            rr = r
            min(ll, l)
    
    print(rr - ll + 1)
    
for _ in range(t):
    case()