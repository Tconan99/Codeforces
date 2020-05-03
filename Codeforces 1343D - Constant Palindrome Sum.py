# https://codeforces.com/problemset/problem/1343/D

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    k = int(arr[1])

    arr = input().split()
    arr = list(map(int, arr))

    ks = [0] * (2 * k + 1)
    # print(ks)
    for i in range(int(n/2)):
        for j in range(2, 2 * k + 1):
            left = arr[i]
            right = arr[n - i - 1]
            if left + right == j:
                ks[j] += 0
            else:
                if left >= j and right >= j:
                    ks[j] += 2
                elif left + k < j and right + k < j:
                    ks[j] += 2
                else:
                    ks[j] += 1


    print(min(ks[2:]))
