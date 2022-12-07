# source : https://www.acmicpc.net/problem/10865

import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())

count = [0] * (n + 1)
for _ in range(m):
    # input
    a, b = map(int, input().split())
    
    count[a] += 1
    count[b] += 1

for cnt in count[1:]:
    print(cnt)