# https://codeforces.com/problemset/problem/1367/C
 
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
 
def case():
    arr = list(map(int, input().split(" ")))
    n, k = arr[0], arr[1]
    arr = input()

    startOne = False
    length = 0
    result = 0
    for value in arr:
        if value == '1':
            length = max(0, length - k)
            if startOne:
                length = max(0, length - k)
            result += length // (k + 1) + (1 if length % (k + 1) > 0 else 0) 
            startOne = True
            length = 0
        else:
            length += 1

    if startOne:
        length = max(0, length - k)
    result += length // (k + 1) + (1 if length % (k + 1) > 0 else 0)

    print(result)

for _ in range(t):
    case()