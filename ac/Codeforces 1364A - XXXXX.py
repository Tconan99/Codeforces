# https://codeforces.com/problemset/problem/1364/A
 
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
 
t = int(input())
 
def printd(value):
    # print(value)
    pass
 
def case():
    arr = list(map(int, input().split(" ")))
    n, x = arr[0], arr[1]
    arr = list(map(int, input().split(" ")))

    sum = 0
    left = -1
    right = -1

    # 计算总和 与 左边最近非 x 倍数的个数
    for index, value in enumerate(arr):
        sum += value
        if left == -1 and value % x != 0:
            left = index
    
        if value % x != 0:
            right = index
    
    pos = -1
    if left >= 0:
        pos = left + 1

    # 计算右边和左边最近非 x 倍数的个数
    if right >= 0:
        pos2 = n - right
        if pos > 0:
            pos = min(pos, pos2)
    
    # 统计答案
    result = n
    if sum % x == 0:
        if pos > 0:
            result -= pos
        else:
            result = -1

    print(result)

for _ in range(t):
    case()