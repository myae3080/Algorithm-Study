# source : https://www.acmicpc.net/problem/2738
# math

# input
n, m = map(int, input().split())

a, b, result = [], [], []

# input
[a.append(list(map(int, input().split()))) for _ in range(n)]
[b.append(list(map(int, input().split()))) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    
    print()