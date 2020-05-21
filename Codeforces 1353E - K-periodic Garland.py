# https://codeforces.com/contest/1353/problem/E

import sys
import os
import heapq

try:
    path = "./file/input.txt"
    if os.path.exists(path):
        sys.stdin = open(path, 'r')
    # sys.stdout = open(r"./file/output.txt", 'w')
except:
    pass

t = int(input())

def printd(value):
    # print(value)
    pass

for _ in range(t):
    arr = list(map(int, input().split(" ")))
    n, k = arr[0], arr[1]
    str = input()
    count = len(str)
    leftone = [0] * count
    leftzero = [0] * count
    rightone = [0] * count
    rightzero = [0] * count

    one = [0] * count
    # zero = [0] * count

    sum = 0
    for i, c in enumerate(str):
        if i > 0:
            sum += 1 if str[i - 1] == '1' else 0

        if i >= k:
            sum -= 1 if str[i - k] == '1' else 0

        one[i] = sum

    printd(str)
    printd(one)

    for i, c in enumerate(str):
        number = 1 if c == '0' else 0
        numberzero = 0 if c == '0' else 1
        if i >= k:
            number += min(leftone[i - k], leftzero[i - k])
            numberzero += leftzero[i - k]
        leftone[i] = one[i] + number
        leftzero[i] = one[i] + numberzero
    
    printd(leftone)
    printd(leftzero)

    printd("--right---")

    str = str[::-1]
    sum = 0
    for i, c in enumerate(str):
        if i > 0:
            sum += 1 if str[i - 1] == '1' else 0

        if i >= k:
            sum -= 1 if str[i - k] == '1' else 0

        one[i] = sum


    printd(str)
    printd(one)

    for i, c in enumerate(str):
        number = 1 if c == '0' else 0
        numberzero = 0 if c == '0' else 1
        if i >= k:
            number += min(rightone[i - k], rightzero[i - k])
            numberzero += rightzero[i - k]
        rightone[i] = one[i] + number
        rightzero[i] = one[i] + numberzero
    
    printd(rightone)
    printd(rightzero)

    leftone.reverse()
    leftzero.reverse()

    result = 99999999
    for i, c in enumerate(str):
        value = leftone[i] + rightone[i]
        value -= 1 if c == '0' else 0
        result = min(result, value)

        value = leftzero[i] + rightzero[i]
        value -= 0 if c == '0' else 1
        result = min(result, value)

    print(result)