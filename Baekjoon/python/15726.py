# source : https://www.acmicpc.net/problem/15726

# input
a, b, c = map(int, input().split())

print(a * max(b, c) // min(b, c))