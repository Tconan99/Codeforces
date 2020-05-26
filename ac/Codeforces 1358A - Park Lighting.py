# https://codeforces.com/problemset/problem/1358/B

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
    (n, m) = arr[0], arr[1]
    
    result = 0
    if m % 2 == 1:
        result += int(n / 2)
        if n % 2 == 1:
            result += 1
    
    result += n * int(m / 2)
    print(result)