# source : https://www.acmicpc.net/problem/23253

import sys

is_possible = True

# input
input = sys.stdin.readline
n, m = map(int, input().split())

for _ in range(m):
    # input
    i = int(input())
    k = list(map(int, input().split()))
    
    if k != sorted(k, reverse=True):
        is_possible = False

print('Yes') if is_possible else print('No')