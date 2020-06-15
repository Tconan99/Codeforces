# https://codeforces.com/problemset/problem/1354/A
 
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
    a, b, c, d = arr[0], arr[1], arr[2], arr[3]
    if a > 0:
        a -= b
    
    if a > 0:
        if d >= c:
            print(-1)
        else:
            count =  a // (c - d)
            if a % (c - d) != 0:
                count += 1
            print(b + count * c) 
    else:
        print(b)

for _ in range(t):
    case()