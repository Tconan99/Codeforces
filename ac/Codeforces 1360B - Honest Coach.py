# https://codeforces.com/contest/1353/problem/E

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
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    result = 20000
    for i in range(1, n):
        value = arr[i] - arr[i - 1]
        if value < result:
            result = value
    print(result)
    
    
