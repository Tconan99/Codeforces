# https://codeforces.com/problemset/problem/1343/A

import math
import sys

# sys.stdin = open('in.txt', 'r')
# sys.stdout = open('out.txt', 'w')

t = int(input())
for index in range(t):
    n = int(input())
    k = 2
    while True:
        sum = int(math.pow(2, k) - 1)
        if n % sum == 0:
            break
        k += 1
    
    x = int(n / sum)
    print(x)