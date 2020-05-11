# https://codeforces.com/problemset/problem/1352/C

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    k = int(arr[1])

    print(int(k / (n - 1)) * n  + (-1 if k % (n - 1) == 0 else k % (n - 1)))