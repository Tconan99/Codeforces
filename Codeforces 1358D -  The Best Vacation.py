# https://codeforces.com/contest/1358/problem/D
 
import sys
import os
import heapq
import math
 
try:
    path = "./file/input.txt"
    if os.path.exists(path):
        sys.stdin = open(path, 'r')
    # sys.stdout = open(r"./file/output.txt", 'w')
except:
    pass
 
t = 1
 
def printd(value):
    # print(value)
    pass
 
def case():
    arr = list(map(int, input().split(" ")))
    n, x = arr[0], arr[1]
    arr = list(map(int, input().split(" ")))

    arr = arr * 2
    result = [0] * len(arr)
    total = [0] * len(arr)
    left = 0
    right = 0
    sum = arr[0]
    result[0] = arr[0]
    total[0] += int((1 + arr[0]) * arr[0] / 2)

    while right < n * 2:
        while sum < x and right < n * 2:
            right += 1
            sum += arr[right]
            result[right] = sum
            total[right] += int((1 + arr[right]) * arr[right] / 2)

            while left < right and sum > x:
                sum -= arr[left]
                total[right] -= int((1 + arr[left]) * arr[left] / 2)
                result[right] = sum
                left += 1

        right += 1
        if right >= n * 2:
            break

        while left < right and sum > x:
            sum -= arr[left]
            total[right] -= int((1 + arr[left]) * arr[left] / 2)
            result[right] = sum
            left += 1
    
    answer = 0
    for index in range(n * 2):
        if result[index] >= x:
            diff = result[index] - x
            value = total[index] - int((1 + diff) * diff / 2) 
            answer = max(answer, value)
    
    print(answer)

for _ in range(t):
    case()