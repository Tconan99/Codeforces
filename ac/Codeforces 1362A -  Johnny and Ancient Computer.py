# https://codeforces.com/problemset/problem/1362/A
 
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
    a, b = arr[0], arr[1]
    
    if a == b:
        print(0)
        return
 
    if a > b:
        b, a = a, b
 
    result = 0
    while a < b:
        a *= 2
        result += 1
 
    if a == b:
        print(int(result / 3) + (1 if result % 3 > 0 else 0))
        return
        
    print(-1)
 
for _ in range(t):
    case()