# https://codeforces.com/problemset/problem/1342/A

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    x = int(arr[0])
    y = int(arr[1])

    if x > y:
        x, y = y, x

    arr = input().split(" ")
    a = int(arr[0])
    b = int(arr[1])

    print(min(a * (y - x) + b * x, a * (y + x)))
