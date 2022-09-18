# source : https://www.acmicpc.net/problem/2355

# input
a, b = map(int, input().split())

print((a + b) * (abs(b - a) + 1) // 2)