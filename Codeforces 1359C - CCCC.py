# https://codeforces.com/problemset/problem/1360/F
 
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
 
        start = x - 5
        mm = 9999999999
        index = 0
        for i in range(start, start + 15):
            ttt = abs((h * i + c * (i - 1)) / (i * 2 - 1) - t)
            if mm > ttt or (mm >= ttt and index < i):
                mm = ttt
                index = i
                result = i * 2 - 1
                
    print(result)
 