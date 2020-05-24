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
    arr = list(map(int, input().split(" ")))
    n, k = arr[0], arr[1]
    for i in range(k, 0, -1):
        if n % i == 0:
            number = int(n / i)
            print(number)
            break
    
    
    
