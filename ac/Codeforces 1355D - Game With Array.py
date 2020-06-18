# https://codeforces.com/problemset/problem/1355/D
 
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
 
t = 1
 
def printd(value):
    # print(value)
    pass
 
def case():
    arr = list(map(int, input().split(" ")))
    n, s = arr[0], arr[1]
    right = s - n + 1
    left = n - 1
    k = left + 1
    if k < right:
        print("YES")
        result = [1] * left
        result.append(right)
        print(" ".join(str(i) for i in result)) 
        print(k)
    else:
        print("NO")

for _ in range(t):
    case()