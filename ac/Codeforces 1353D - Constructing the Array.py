# https://codeforces.com/contest/1353/problem/D

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

class Node:
    def __init__(self, n, left, right):
        self.left = left
        self.right = right
        self.weight = n - right + left

    def __lt__(self, other):
        return self.weight < other.weight or (self.weight == other.weight and self.left < other.left)

t = int(input())

for _ in range(t):
    n = int(input())

    q = []
    result = [0] * (n + 1)
    heapq.heappush(q, Node(n, 1, n))

    index = 1
    while True:
        if len(q) == 0:
            break

        node = heapq.heappop(q)
        if node is None:
            break
        
        if node.left == node.right:
            result[node.left] = index
            index += 1
        else:
            middle = int((node.left + node.right) / 2)
            result[middle] = index
            index += 1

            if node.left != middle:
                heapq.heappush(q, Node(n, node.left, middle - 1))
            heapq.heappush(q, Node(n, middle + 1, node.right))

    print(" ".join(str(i) for i in result[1:]))