# source : https://www.acmicpc.net/problem/2167
# prefix sum

import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())

# input
table = [list(map(int, input().split())) for _ in range(n)]

sums = [[0] * (m + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, m + 1):
        sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + table[i - 1][j - 1]
        
for _ in range(int(input())):
    # input
    x1, y1, x2, y2 = map(int, input().split())
    
    print(sums[x2][y2] - sums[x2][y1 - 1] - sums[x1 - 1][y2] + sums[x1 - 1][y1 - 1])