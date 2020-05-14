# https://codeforces.com/problemset/problem/1352/G

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split(" ")))
    a = arr[0]
    b = arr[1]
    c = arr[2]

    result = ""

    end = -1
    if a > 0:
        result += "0" * (a + 1)
        end = 0

    if c > 0:
        result += "1" * (c + 1)
        end = 1

    if end == -1:
        result = "1"
        end = 1

    if "01" in result:
        b -= 1

    for _ in range(b):
        if end == 1:
            result += "0"
        else:
            result += "1"
        end = 1 - end

    print(result)