# source : https://www.acmicpc.net/problem/3034
# math

# input
n, w, h = map(int, input().split())
d = int(((w ** 2) + (h **2)) ** 0.5)

for _ in range(n):
    # input
    m = int(input())

    [print('DA') if m <= w or m <= h or m <= d else print('NE')]