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

    ks = [0] * (2 * k + 2)
    # print(ks)
    for i in range(int(n/2)):
        left = arr[i]
        right = arr[n - i - 1]

        if left > right:
            left, right = right, left

        """
        2 : [2, left], 
        1 ：[left + 1, left + right - 1]
        0 : [left + right, left + right]
        1 : [left + right + 1, right + k]
        2 : [right + k + 1, 2*k]
        """

        ks[2] += 2
        ks[left + 1] -= 1
        ks[left + right] -= 1
        ks[left + right + 1] += 1
        ks[right + k + 1] += 1

    sum = 0
    minvalue = 99999999
    for i in range(2, k * 2 + 1):
        sum += ks[i]
        minvalue = min(minvalue, sum)
    
    print(minvalue)

