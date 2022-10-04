# source : https://www.acmicpc.net/problem/25238

# input
a, b = map(int, input().split())

print(0) if (a * (100 - b) / 100) >= 100 else print(1)