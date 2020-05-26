# https://codeforces.com/contest/1358/problem/A

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
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort()
    result = 0
    for index, number in enumerate(a):
        count = index + 1
        if count >= number:
            result =  count
    print(result + 1)