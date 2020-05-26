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

for _ in range(t):
    arr = list(map(int, input().split(" ")))
    (n, k) = arr[0], arr[1]
    s = list(map(int, input().split(" ")))


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
                isSuccess = True
                break

            if s[pos] == k:
                break

            pos += 1

        i = pos
        
        if isSuccess:
            break

    if not isSuccess:
        s = s[::-1]
        i = 0
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
                    isSuccess = True
                    break

                if s[pos] == k:
                    break

                pos += 1
            
            i = pos
            
            if isSuccess:
                break
    
    print("yes" if isSuccess else "no")