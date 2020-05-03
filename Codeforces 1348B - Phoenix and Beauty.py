# https://codeforces.com/problemset/problem/1348/B

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    line = input()
    arr = line.split(" ")
    n = int(arr[0])
    k = int(arr[1])
    line = input()
    arr = line.split(" ")
    num = []
    diff = []
    result = []
    for i in arr:
        integer = int(i)
        num.append(integer)
        if integer not in diff:
            diff.append(integer)
        
    if len(diff) > k:
        print(-1)
    else:
        while len(diff) < k:
            for i in range(1, n + 1):
                if i not in diff:
                    diff.append(i)
                    break
        pos = -1
        for i in num:
            while pos < len(diff):
                pos += 1
                if pos == len(diff):
                    pos = 0

                result.append(diff[pos])
                if diff[pos] == i:
                    break
        
        print(len(result))
        print(" ".join(str(i) for i in result))


    