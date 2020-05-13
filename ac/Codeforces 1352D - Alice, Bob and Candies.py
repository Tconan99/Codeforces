# https://codeforces.com/problemset/problem/1352/D

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split(" ")
    arr = list(map(int, arr))
    # print(arr)

    step = 0
    l = 0
    r = n - 1
    last = 0
    lvalue = 0
    rvalue = 0
    while l <= r:
        temp = 0
        while temp <= last and l <= r:
            temp += arr[l]
            l += 1
        if temp > 0:
            step += 1
            last = temp
            lvalue += temp

        temp = 0
        while temp <= last and l <= r:
            temp += arr[r]
            r -= 1
        
        if temp > 0:
            step += 1
            last = temp
            rvalue += temp
    
    print(step, lvalue, rvalue)
