# https://codeforces.com/problemset/problem/1367/B
 
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
    arr = list(map(int, input().split(" ")))

    num = 0
    result = 0
    for index, value in enumerate(arr):
        num += (1 if value % 2 == 0 else -1)
        if index % 2 == 0 and value % 2 != 0:
            result += 1
    print(result if num == 0 or num == 1 else -1)
    
for _ in range(t):
    case()