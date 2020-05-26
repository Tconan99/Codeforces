# https://codeforces.com/contest/1360/problem/F

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

def run(n, k, s):
    i = 0
    isSuccess = True if len(s) == 1 and s[0] == k else False
    while i < n:
        if s[i] != k:
            i += 1
            continue
        
        blow = 0
        biger = 0
        pos = i + 1
        while pos < n:

            if s[pos] >= k:
                biger += 1
            else:
                blow += 1

            if biger - blow == 0 or biger - blow == 1:
                return True

            if s[pos] == k:
                break

            pos += 1

        i = pos
    return isSuccess

def case():
    arr = list(map(int, input().split(" ")))
    (n, k) = arr[0], arr[1]
    s = list(map(int, input().split(" ")))

    isSuccess = run(n, k, s)
    isSuccess = isSuccess or run(n, k, s[::-1])
    
    print("yes" if isSuccess else "no")

for _ in range(t):
    case()