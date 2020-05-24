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
    
    isYes = False
    even = 0
    odd = 0
    for i in range(0, n):
        if i > 0:
            if arr[i] - arr[i - 1] == 1:
                isYes = True
        if arr[i] % 2 == 0:
            even += 1

    if even % 2 == 0:
        isYes = True        

    print("YES" if isYes else "NO")
    
    
