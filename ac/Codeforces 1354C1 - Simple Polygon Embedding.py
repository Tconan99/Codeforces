# https://codeforces.com/problemset/problem/1354/C1
 
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
    n = int(input())
    result = 1 / math.tan(math.pi * 2 / (n * 4))
    print(result)

for _ in range(t):
    case()