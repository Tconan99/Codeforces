# https://codeforces.com/problemset/problem/1355/B
 
import sys
import os
import heapq
import math
import time
 
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
    count = [0] * (n + 1)
    e = list(map(int, input().split(" ")))
    for number in e:
        count[number] += 1
    
    result = 0
    for index, c in enumerate(count):
        if index == 0:
            continue

        if c >= index:
            result += c // index

        if c % index != 0 and index < n:
            count[index + 1] += c % index
    
    # print(result)
    return result

# start = time.time()

result = ""
for _ in range(t):
    result += str(case()) + "\n"

print(result, end="")
# print(time.time() - start)