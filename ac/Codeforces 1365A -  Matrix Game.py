# https://codeforces.com/problemset/problem/1365/A
 
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
    n, m = arr[0], arr[1]

    matrix = []
    for row in range(n):
        rows = list(map(int, input().split(" ")))
        matrix.append(rows)
    
    empty_row_count = 0
    for row in range(n):
        count = 1
        for col in range(m):
            if matrix[row][col] == 1:
                count = 0
        empty_row_count += count
    
    empty_col_count = 0
    for col in range(m):
        count = 1
        for row in range(n):
            if matrix[row][col] == 1:
                count = 0
        empty_col_count += count
    
    print("Ashish" if min(empty_row_count, empty_col_count) % 2 == 1 else "Vivek")

for _ in range(t):
    case()