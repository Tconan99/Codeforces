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
    x = 1 / math.sin(math.pi / (2 * n))
    print(x)

for _ in range(t):
    case()