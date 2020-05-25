# https://codeforces.com/problemset/problem/1360/E

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
    m = []
    for _ in range(n):
        arr = input()
        m.append(arr)

    result = 'YES'
    for row in range(n - 2, -1, -1):
        # line
        for col in range(row - 1, -1, -1):
            if m[row][col] == '1':
                if m[row + 1][col] != '1' and m[row][col + 1] != '1':
                    result = 'NO'
        
        # col
        for col in range(row, -1, -1):
            if m[col][row] == '1':
                if m[col + 1][row] != '1' and m[col][row + 1] != '1':
                    result = 'NO'
        
    print(result)