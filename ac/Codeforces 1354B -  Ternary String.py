# https://codeforces.com/problemset/problem/1354/B
 
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
    string = input()
    one = -1
    two = -1
    three = -1
    result = len(string) + 1
    for index, c in enumerate(string):
        if c == '1':
            one = 0
        elif index > 0 and one >= 0:
            one = one + 1

        if c == '2':
            two = 0
        elif index > 0 and two >= 0:
            two = two + 1

        if c == '3':
            three = 0
        elif index > 0 and three >= 0:
            three = three + 1

        if one >= 0 and two >= 0 and three >= 0:
            result = min(result, max(one, two, three))
    
    if result == len(string) + 1:
        result = -1
        
    print(result + 1)

for _ in range(t):
    case()