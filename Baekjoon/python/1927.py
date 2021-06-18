# data structure, priority queue, heapq

import sys
import heapq

# input
input = sys.stdin.readline
n = int(input())

heap = []

for i in range(n):
    num = int(input())

    if num != 0:
        heapq.heappush(heap, num)
    else:
        print(heapq.heappop(heap)) if heap else print(0)