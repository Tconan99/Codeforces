# https://codeforces.com/problemset/problem/1360/A

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
    arr = list(map(int, input().split(" ")))
    a, b = arr[0], arr[1]
    if a > b:
        b *= 2
    else:
        a *= 2
    if a > b:
        result = a * a
    else:
        result = b * b
    print(result)
    
