# https://codeforces.com/problemset/problem/1359/C
 
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
 
T = int(input())
 
def printd(value):
    # print(value)
    pass
 
for _ in range(T):
    arr = list(map(int, input().split(" ")))
    h, c, t = arr[0], arr[1], arr[2]
    
    result = 1
    if t == h:
        result = 1
    elif t * 2 <= (h + c):
        result = 2
    elif t * 3 >= (h * 2 + c):
        result = 1 if abs(h * 3 - t * 3) <= abs((h * 2 + c) - t * 3) else 3
    else:
        x = (t - c) / (2 * t - h - c)
        x = int(x)
 
        start = max(2, x - 5)
        top = 99999999999
        bottom = 1
        for i in range(start, start + 15):
            bottomi = abs(i * 2 - 1)
            topi = abs((h * i + c * (i - 1)) - bottomi * t)
            if top * bottomi > topi * bottom:
                top = topi
                bottom = bottomi
                result = i * 2 - 1
                
    print(result)
 