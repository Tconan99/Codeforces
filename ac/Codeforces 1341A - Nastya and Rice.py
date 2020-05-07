# https://codeforces.com/problemset/problem/1341/A

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    a = int(arr[1])
    b = int(arr[2])
    c = int(arr[3])
    d = int(arr[4])

    pilemin = n * (a - b)
    pilemax = n * (a + b)

    packagemin = c - d
    packagemax = c + d

    if pilemin <= packagemax and pilemax >= packagemin:
        print("Yes")
    else:
        print("No")
