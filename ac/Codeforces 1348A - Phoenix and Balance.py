# https://codeforces.com/problemset/problem/1348/A

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    left = 0
    for index in range(n - int(n / 2), n):
        left += pow(2, index)
    right = 0
    for index in range(1, int(n / 2)):
        right += pow(2, index)
    right += pow(2, n)

    diff = right - left
    print(diff)