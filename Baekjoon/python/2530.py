# source : https://www.acmicpc.net/problem/2530
# math

# input
h, m, s = map(int, input().split())
seconds = int(input())

# 초 계산
s += (seconds % 60)
seconds //= 60

if s >= 60:
    s -= 60
    m += 1

# 분 계산
m += (seconds % 60)
seconds //= 60

if m >= 60:
    m -= 60
    h += 1

# 시간 계산
h += seconds

while h >= 24:
    h -= 24
    
print(h, m, s)