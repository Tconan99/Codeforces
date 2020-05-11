# https://codeforces.com/problemset/problem/1345/A

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    m = int(arr[1])
    
    if n == 1 or m == 1 or (n == 2 and m == 2):
        print("YES")
    else:
        print("NO")