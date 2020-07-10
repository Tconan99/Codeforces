# https://codeforces.com/problemset/problem/1364/B

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
    # The first line contains an integer 𝑡 (1≤𝑡≤2⋅104) — the number of test cases. The description of the test cases follows.
    # The first line of each test case contains an integer 𝑛 (2≤𝑛≤105) — the length of the permutation 𝑝.
    # The second line of each test case contains 𝑛 integers 𝑝1, 𝑝2, …, 𝑝𝑛 (1≤𝑝𝑖≤𝑛, 𝑝𝑖 are distinct) — the elements of the permutation 𝑝.
    # The sum of 𝑛 across the test cases doesn't exceed 105.

    n = int(input())
    p = list(map(int, input().split(" ")))
    #  𝑛, 𝑥 and 𝑚

    first = p[0]
    result = [first]
    for index in range(2, n):
        value = p[index]
        last = p[index - 1]
        if not ((first > last and last > value) or (first < last and last < value)):
            result.append(last)
            first = last

    result.append(p[n-1])
        
    print(len(result))
    print(" ".join(str(i) for i in result))
    
for _ in range(t):
    case()