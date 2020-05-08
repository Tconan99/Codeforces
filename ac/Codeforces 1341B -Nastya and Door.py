# https://codeforces.com/problemset/problem/1341/B

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    k = int(arr[1])

    arr = input().split(" ")
    arr = list(map(int, arr))
    isPeek = [False]
    for i in range(1, n - 1):
        isPeek.append(arr[i] > max(arr[i - 1], arr[i + 1]))
    isPeek.append(False)

    num = 0
    left = 0
    right = k
    for i in range(k - 1):
        num += (1 if isPeek[i] else 0)

    maxvalue = num
    minleft = 0
    
    for r in range(k, n):
        left += 1
        if isPeek[left]:
            num -= 1
        if isPeek[r - 1]:
            num += 1
        
        if num > maxvalue:
            minleft = left
            maxvalue = num
    
    print(maxvalue + 1, minleft + 1)
