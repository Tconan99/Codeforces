# https://codeforces.com/problemset/problem/1363/B

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

graph = []
x = 0

def dfs(depth, index):
    global graph

    if len(graph[index]) <= 1 and index == x:
        return 1

    if len(graph[index]) == 0:
        return 1

    sumvalue = 1
    maxvalue = 0    

    for value in graph[index]:
        graph[value].remove(index)
        result = dfs(depth + 1, value)

        sumvalue += result

    if x == index:
        sumvalue -= 1

    return sumvalue

def case():
    global x
    arr = list(map(int, input().split(" ")))
    n, x = arr[0], arr[1]

    global graph
    graph = []

    for _ in range(n + 1):
        graph.append([])

    for _ in range(n - 1):
        arr = list(map(int, input().split(" ")))
        a, b = arr[0], arr[1]
        
        graph[a].append(b)
        graph[b].append(a)

    print("Ayush" if dfs(1, x) % 2 == 1 else "Ashish")

for _ in range(t):
    case()