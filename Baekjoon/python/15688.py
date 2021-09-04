# soucre : https://www.acmicpc.net/problem/15688
# sorting

import sys

# input
input = sys.stdin.readline

sorting = []

for _ in range(int(input())):
    # input
    sorting.append(int(input()))

sorting.sort()

for i in sorting:
    print(i)