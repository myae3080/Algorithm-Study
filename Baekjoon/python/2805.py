# binary search

import sys

# input
input = sys.stdin.readline
n, h = map(int, input().split())
tree_list = list(map(int, input().split()))

start, end = 0, max(tree_list)

while start <= end:
    mid = (start + end) // 2
    tree_length = sum([t - mid for t in tree_list if t - mid > 0])

    if tree_length >= h:
        start = mid + 1
    else:
        end = mid - 1

print(end)