# source : https://www.acmicpc.net/problem/10813

# input
n, m = map(int, input().split())

baskets = {}

for i in range(n):
    baskets[i + 1] = i + 1
    
for _ in range(m):
    # input
    i, j = map(int, input().split())
    
    baskets[i], baskets[j] = baskets[j], baskets[i]
    
[print(baskets[i + 1], end=' ') for i in range(n)]