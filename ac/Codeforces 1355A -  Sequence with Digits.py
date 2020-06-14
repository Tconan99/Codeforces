# https://codeforces.com/contest/1358/problem/D
 
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
    a, k = arr[0], arr[1]
    for index in range(k - 1):
        mindigit = 9
        maxdigit = 0
        number = a
        while number > 0:
            digit = number % 10
            number //= 10
            maxdigit = max(maxdigit, digit)
            mindigit = min(mindigit, digit)
        
        if mindigit == 0:
            break
            
        a += maxdigit * mindigit
    
    print(a)

for _ in range(t):
    case()