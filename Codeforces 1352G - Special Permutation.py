# https://codeforces.com/problemset/problem/1352/D

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    result = [3, 1, 4, 2]
    for i in range(5, n + 1):
        if i % 2 == 1:
            result.append(i)

    result.reverse()
    for i in range(5, n + 1):
        if i % 2 == 0:
            result.append(i)

    if n >= 4:
        print(" ".join(str(i) for i in result))
    else:
        print(-1)