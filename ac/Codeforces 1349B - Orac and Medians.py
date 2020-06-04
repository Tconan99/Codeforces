# https://codeforces.com/problemset/problem/1349/B

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
    have = False
    isSuccess = True if len(s) == 1 and s[0] == k else False
    while i < n:
        if s[i] == k:
            have = True
        if i < n - 1 and s[i] >= k and s[i + 1] >= k:
            isSuccess = True
        if i < n - 2 and s[i] >= k and s[i + 2] >= k:
            isSuccess = True
        i += 1

    return isSuccess and have

def case():
    arr = list(map(int, input().split(" ")))
    (n, k) = arr[0], arr[1]
    s = list(map(int, input().split(" ")))
    
    print("yes" if run(n, k, s) else "no")

for _ in range(t):
    case()