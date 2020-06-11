# https://codeforces.com/problemset/problem/1362/C
 
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
    bit = 1
    result = 0
    while n > 0:
        if n & 1 == 1:
            result += 2**bit - 1
        bit += 1
        n = n >> 1
    print(result)

for _ in range(t):
    case()