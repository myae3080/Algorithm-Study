# source : https://www.acmicpc.net/problem/20551
# data structure, sorting, binary search

import sys
input = sys.stdin.readline

a = []

# input
n, m = map(int, input().split())
[a.append(int(input())) for _ in range(n)]

a.sort()

for __ in range(m):
    # input
    d = int(input())
    
    start, end, target_idx = 0, len(a) - 1, -1
    
    while start <= end:
        mid = (start + end) // 2
        temp = a[mid]
        
        if temp > d:
            end = mid - 1
        elif temp < d:
            start = mid + 1
        else:
            if end == mid:
                target_idx = mid
                break
            else:
                end = mid
        
    print(target_idx)