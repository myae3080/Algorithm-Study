# source : https://www.acmicpc.net/problem/1267

y, m = 0, 0

# input
n = int(input())
times = list(map(int, input().split()))

for time in times:
    y += (time // 30) * 10 + 10
    m += (time // 60) * 15 + 15
    
print('Y', 'M', y) if y == m else print('M', m) if y > m else print('Y', y)