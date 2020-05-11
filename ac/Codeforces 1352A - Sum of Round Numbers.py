# https://codeforces.com/problemset/problem/1352/A

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    pos = 0
    while n > 0:
        if n % 10 > 0:
            result.append((n % 10) * pow(10, pos))
        n = int(n / 10)
        pos += 1
    
    print(len(result))
    print(" ".join(str(i) for i in result)) 