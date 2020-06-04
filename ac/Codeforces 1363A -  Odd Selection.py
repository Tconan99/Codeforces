# https://codeforces.com/problemset/problem/1363/A

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
    n, k = arr[0], arr[1]
    arr = list(map(int, input().split(" ")))

    odd = 0
    even = 0
    for number in arr:
        if number % 2 == 1:
            odd += 1
        else:
            even += 1

    k = max(1, k - even)
    if k % 2 == 0 and even > 0:
        k += 1
    
    if odd >= k and k % 2 == 1:
        print("Yes")
    else:
        print("No")

for _ in range(t):
    case()