# https://codeforces.com/problemset/problem/1359/A

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
    n, m, x, y = arr[0], arr[1], arr[2], arr[3]

    if x * 2 < y:
        y = x * 2
    
    result = 0
    for _ in range(n):
        row = input()
        i = 0
        while i < m:
            if row[i] == '*':
                i += 1
                continue
            else:
                if i < m - 1 and row[i + 1] == '.':
                    result += y
                    i += 2
                else:
                    result += x
                    i+= 1
    print(result)