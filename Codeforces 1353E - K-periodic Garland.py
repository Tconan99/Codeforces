# https://codeforces.com/contest/1353/problem/E

import sys
import os
import heapq

try:
    path = "./file/input.txt"
    if os.path.exists(path):
        sys.stdin = open(path, 'r')
    # sys.stdout = open(r"./file/output.txt", 'w')
except:
    pass

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split(" ")))
    n, k = arr[0], arr[1]
    str = input().strip("0")
    count = len(str)
    left = [0] * count
    right = [0] * count

    one = [0] * count

    sum= 0
    for i, c in enumerate(str):
        if i > 0:
            sum += 1 if str[i - 1] == '1' else 0

        if i >= k:
            sum -= 1 if str[i - k] == '1' else 0

        one[i] = sum

    # print(str)
    # print(one)

    for i, c in enumerate(str):
        number = one[i]
        number += 1 if c == '0' else 0
        if i >= k:
            number += left[i - k]
        left[i] = number
    
    # print(left)

    # print("--right---")

    str = str[::-1]
    sum= 0
    for i, c in enumerate(str):
        if i > 0:
            sum += 1 if str[i - 1] == '1' else 0

        if i >= k:
            sum -= 1 if str[i - k] == '1' else 0

        one[i] = sum

    # print(str)
    # print(one)

    for i, c in enumerate(str):
        number = one[i]
        number += 1 if c == '0' else 0
        if i >= k:
            number += right[i - k]
        right[i] = number
    
    # print(right)

    left.reverse()

    result = 99999999
    for i, c in enumerate(str):
        value = left[i] + right[i]
        value -= 1 if c == '0' else 0
        result = min(result, value)

    print(result)

        