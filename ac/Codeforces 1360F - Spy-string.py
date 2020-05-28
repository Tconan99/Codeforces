# https://codeforces.com/problemset/problem/1360/F

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
    n, m = arr[0], arr[1]
    a = []
    for _ in range(n):
        a.append(input())

    result = -1

    for i in range(m):

        success = True
        chars = []
        for row in range(1, n):
            count = 0
            for pos in range(m):
                if pos != i:
                    if a[0][pos] != a[row][pos]:
                        count += 1
            if count > 1:
                success = False
                break
            elif count == 1:
                if a[row][i] not in chars:
                    chars.append(a[row][i])
        if not success:
            continue

        if len(chars) == 1:
            result = a[0]
            result = result[0:i] + chars[0] + result[i + 1:]
            break
        elif len(chars) == 0:
            result = a[0]
            break
    
    print(result)