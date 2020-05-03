# https://codeforces.com/problemset/problem/1343/B

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for i in range(t):
    n = int(input())
    count = int(n / 2)
    if count % 2 == 1:
        print("NO")
    else:
        print("YES")
        for j in range(1, count + 1):
            if j != 1:
                print(" ", end="")
            print(j * 2, end="")

        for j in range(1, count + 1):
            print(" ", end="")
            if j == count:
                print(j * 2 + count - 1)
            else:
                print(j * 2 - 1, end="")
