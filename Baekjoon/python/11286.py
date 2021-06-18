# data structure, priority queue, heapq

import sys
import heapq

# input
input = sys.stdin.readline

heap = []

for i in range(int(input())):
    num = int(input())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)