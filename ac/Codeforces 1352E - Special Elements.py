# https://codeforces.com/problemset/problem/1352/E

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split(" ")
    arr = list(map(int, arr))
    # print(arr)

    number = [0] * (n + 1)
    add = [0] * (n + 1)
    result = 0

    for a in arr:
        number[a] += 1

    for i, a in enumerate(arr):
        for j in range(i + 1):
            add[j] += a
            if j < i and add[j] <= n:
                result += number[add[j]]
                number[add[j]] = 0

    print(result)


