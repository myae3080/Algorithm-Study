# source : https://www.acmicpc.net/problem/10093

# input
a, b = map(int, input().split())

start, end = min(a, b), max(a, b)

print(end - start - 1) if end - start - 1 >= 0 else print(0)
[print(n, end=' ') for n in range(start + 1, end)]