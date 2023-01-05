# source : https://www.acmicpc.net/problem/25756

# input
n = int(input())
def_ignores = list(map(int, input().split()))

v = 0

for di in def_ignores:
    v = 1 - ((1 - v) * (1 - (di / 100)))
    print(round(v * 100, 6))