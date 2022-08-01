# source : https://www.acmicpc.net/problem/1236

# input
n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

row, col = 0, m

# row
for i in range(n):
    if castle[i].count('X') == 0:
        row += 1
    
# col
for i in range(m):
    for j in range(n):
        if castle[j][i] == 'X':
            col -= 1
            break

print(max(row, col))