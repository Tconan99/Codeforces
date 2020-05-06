# https://codeforces.com/problemset/problem/1342/B

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    str = input()

    result = ""
    index = 0
    if '0' in str and '1' in str:
        for c in str:
            result += "01"
    else:
        result = str
    print(result)