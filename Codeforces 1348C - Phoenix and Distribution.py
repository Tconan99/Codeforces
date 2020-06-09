# https://codeforces.com/contest/1348/problem/C

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
    s = input()

    aa = ord('a')

    count = [0] * 26 
    for c in s:
        count[ord(c) - aa] += 1
    
    result = ""
    number = k
    index = 0
    while number > 0 and index < 26:
        if count[index] == 0:
            index += 1
            continue

        if number != k and count[index] >= number:
            number = 0
            result += chr(index + aa)
        
        if count[index] < number:
            number -= count[index]
        else:
            number = k
            result += chr(index + aa)
            index += 1

    print(result)


for _ in range(t):
    case()