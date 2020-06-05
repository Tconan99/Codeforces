# https://codeforces.com/problemset/problem/1363/B

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
    s = input()

    leftzero = [0] * len(s)
    leftone = [0] * len(s)

    for index in range(len(s)):
        if index > 0:
            leftzero[index] = leftzero[index - 1]
            leftone[index] = leftone[index - 1]
        
            if s[index - 1] == '1':
                leftone[index] += 1
            else:
                leftzero[index] += 1

    rightzero = [0] * len(s)
    rightone = [0] * len(s)

    for index in range(len(s) - 1, -1, -1):
        if index < len(s) - 1:
            rightzero[index] = rightzero[index + 1]
            rightone[index] = rightone[index + 1]
        
            if s[index + 1] == '1':
                rightone[index] += 1
            else:
                rightzero[index] += 1

    result = len(s)
    for index, c in enumerate(s):
        result = min(result, leftone[index] + rightone[index] + int(s[index]))
        result = min(result, leftzero[index] + rightzero[index] + 1 - int(s[index]))
        result = min(result, leftzero[index] + rightone[index])
        result = min(result, leftone[index] + rightzero[index])
    
    print(result)

for _ in range(t):
    case()