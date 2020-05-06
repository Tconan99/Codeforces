# https://codeforces.com/problemset/problem/1343/C

import sys

# sys.stdin = open(r"./file/input.txt", 'r')
# sys.stdout = open(r"./file/output.txt", 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    str = input()
    numbers = str.split(" ")
    numbers.append(0)
    last = None
    sum = 0
    for i in numbers:
        number = int(i)
        if last == None:
           last = number
        else:
            if (last < 0 and number < 0) or (last > 0 and number > 0):
                last = max(last, number)
            else:
                sum += last
                last = number
    print(sum)