# https://codeforces.com/problemset/problem/1366/A
 
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
    n, x, m = arr[0], arr[1]
    list = []
    for _ in range(m):
        lr = list(map(int, input().split(" ")))
        list.append((lr[0], lr[1]))
    
    ms = []
    for item in list:
        for 
    
for _ in range(t):
    case()