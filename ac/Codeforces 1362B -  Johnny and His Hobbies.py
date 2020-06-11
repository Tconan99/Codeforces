# https://codeforces.com/problemset/problem/1362/B
 
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

    answer = -1
    arr.sort()
    for index in range(1, 1025):
        result = []
        for number in arr:
            result.append(number ^ index)
        result.sort()

        isSame = True
        for i in range(n):
            if arr[i] != result[i]:
                isSame = False
        if isSame:
            answer = index
            break  
    
    print(answer)
 
for _ in range(t):
    case()