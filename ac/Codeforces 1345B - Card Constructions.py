# https://codeforces.com/problemset/problem/1345/B

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

index = 0
pre = [0] * 300000

def case():
    n = int(input())
    result = 0

    while n >= 2:
        left = 1
        global index
        right = index
        while left < right:
            middle = int((left + right) / 2)
            if pre[middle] > n:
                right = middle - 1
            else:
                left = middle + 1
        
        left -= 2
        left = max(0, left)
        for i in range(left, left + 5):
            if (pre[i] <= n and pre[i + 1] > n) or i == left + 4:
                result += 1
                n -= pre[i]
                break

    print(result)

last = 1
sum = 0
index = 1
while sum < 10**9:
    last = index * 2 + index - 1
    sum += last
    pre[index] = sum
    index += 1
index -= 1

for _ in range(t):
    case()