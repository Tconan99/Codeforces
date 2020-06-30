# https://codeforces.com/problemset/problem/1367/A
 
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
    arr = input()
    result = arr[0]
    for index in range(1, len(arr), 2):
        result += arr[index]

    print(result)
    
for _ in range(t):
    case()