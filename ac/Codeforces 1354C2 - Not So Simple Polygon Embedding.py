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
    ang = 360 / (2 * n)
    x = 0.5 / math.sin(math.radians(ang / 2))
    ang2 = round(n / 4) * ang
    ang1 = 90 - ang2
    
    ans1 = math.sin(math.radians(ang1)) * x / math.sin(math.radians(45))
    ans2 = math.sin(math.radians(ang2)) * x / math.sin(math.radians(45))

    print(ans1 + ans2)

for _ in range(t):
    case()