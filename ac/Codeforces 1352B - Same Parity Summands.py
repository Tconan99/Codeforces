# https://codeforces.com/problemset/problem/1352/B

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    k = int(arr[1])

    digit = 1 if (n - k + 1) % 2 == 1 else 2

    if n % 2 == 1 and k % 2 == 0:
        print("NO")
    elif n < k * digit:
        print("NO")
    else:
        print("YES")
        result = [digit] * (k - 1)
        result.append(n - (k - 1) * digit)
        print(" ".join(str(i) for i in result)) 
    