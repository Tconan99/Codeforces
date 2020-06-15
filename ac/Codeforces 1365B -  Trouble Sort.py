# https://codeforces.com/problemset/problem/1365/B
 
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
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    one = False
    zero = False
    
    answer = True
    for i in range(0, n):
        if i < n - 1:
            if a[i + 1] < a[i]:
                answer = False
        if b[i] == 0:
            one = True
        else:
            zero = True

    print("Yes" if answer or (one and zero) else "No")

for _ in range(t):
    case()