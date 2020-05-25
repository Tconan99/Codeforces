# https://codeforces.com/problemset/problem/1360/D

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
    n, k = arr[0], arr[1]
    result = n
    end = min(k, int(math.sqrt(n)) + 1)
    for i in range(1, end + 1):
        if n % i == 0:
            number = int(n / i)
            if number <= k:
                result = min(result, i)
            if i <= k:
                result = min(number, result)

    print(result)